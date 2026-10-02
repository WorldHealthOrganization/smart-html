#!/usr/bin/env python3
"""
Replace the embedded rendering in *.json.html / *.xml.html / *.ttl.html pages
with an empty <code data-src="..."> that format-loader.js fills by fetching the
raw file. This drops the publisher's element hyperlinks in the code view, and
makes each page roughly the size of its template instead of template + resource.

Also makes sure every converted page loads format-loader.js and that the
loader file exists where the page expects it.

Idempotent: pages that already use data-src are left alone.

Usage:
    python scripts/slim_format_pages.py <dir> [<dir> ...] [--dry-run]
"""

import argparse
import os
import re
import sys

LOADER_JS = """// Format content loader
// This script removes embedded rendered HTML and replaces it with a fetch call
// to load the actual file (json, xml, ttl) dynamically
(function() {
  const code = document.getElementById('format-content');
  if (code && code.hasAttribute('data-src')) {
    const src = code.getAttribute('data-src');
    fetch(src)
      .then(response => response.text())
      .then(text => {
        code.textContent = text;
        Prism.highlightElement(code);
      })
      .catch(error => {
        console.error('Error loading format content:', error);
        code.textContent = 'Error loading content from ' + src;
      });
  }
})();
"""

SUFFIXES = ('.json.html', '.xml.html', '.ttl.html')

# fmt (from file name) -> (pre class, prism language, label in copy button)
FORMATS = {
    'json': ('json', 'json', 'json'),
    'xml': ('xml', 'xml', 'xml'),
    'ttl': ('rdf', 'turtle', 'ttl'),
}

# The publisher emits one block per page; turtle pages may lack the inner <code>.
BLOCK_RE = re.compile(
    rb'<pre\b[^>]*\bclass="(?:json|xml|rdf)"[^>]*>(?:\s*<code[^>]*>)?.*?(?:</code>\s*)?</pre>',
    re.DOTALL)
# Older templates put src before type, so match either attribute order.
CLIPBOARD_RE = re.compile(
    rb'([ \t]*)<script\b[^>]*\bsrc="((?:\.\./)*)assets/js/clipboard-btn\.js"[^>]*>\s*</script>')
LOADER_TAG_RE = re.compile(rb'src="((?:\.\./)*)assets/js/format-loader\.js"')


def raw_file_for(page_path, text, fmt):
    """Name of the raw file the page renders, taken from its 'Raw <fmt>' link."""
    m = re.search(rb'<a href="([^"/]+\.' + fmt.encode() + rb')" no-download="true">', text)
    if m:
        return m.group(1).decode()
    return os.path.basename(page_path)[:-len('.html')]


def new_block(fmt, src):
    pre_class, lang, label = FORMATS[fmt]
    return (
        '<div style="position: relative;">\n'
        '    <button class="btn-copy" style="position: absolute; top: 10px; right: 20px; z-index: 10;"\n'
        f'            title="Click to copy {label}"\n'
        '            data-clipboard-target="#format-content"></button>\n'
        f'    <pre class="{pre_class}" style="white-space: pre; overflow-x: auto;">'
        f'<code id="format-content" class="language-{lang}" data-src="{src}"></code></pre>\n'
        '  </div>'
    ).encode()


def ensure_loader_tag(text):
    """Return (text, assets prefix) with a format-loader.js tag after clipboard-btn.js."""
    m = LOADER_TAG_RE.search(text)
    if m:
        return text, m.group(1).decode()
    m = CLIPBOARD_RE.search(text)
    if not m:
        return text, None
    tag = (m.group(1) + b'<script type="text/javascript" src="' + m.group(2)
           + b'assets/js/format-loader.js"> </script>')
    return text[:m.end()] + b'\n' + tag + text[m.end():], m.group(2).decode()


def slim_page(path, dry_run, stats, loaders):
    with open(path, 'rb') as f:
        text = f.read()
    fmt = path.rsplit('.', 2)[1]

    already = b'data-src=' in text
    if already:
        stats['already'] += 1
        new = text
    else:
        blocks = BLOCK_RE.findall(text)
        if len(blocks) != 1:
            stats['skip_blocks'] += 1
            print(f"  skip ({len(blocks)} code blocks): {path}")
            return
        src = raw_file_for(path, text, fmt)
        if not os.path.isfile(os.path.join(os.path.dirname(path), src)):
            stats['skip_nosrc'] += 1
            print(f"  skip (missing {src}): {path}")
            return
        new = BLOCK_RE.sub(lambda _: new_block(fmt, src), text, count=1)
        stats['converted'] += 1

    new, prefix = ensure_loader_tag(new)
    if prefix is None:
        stats['skip_noanchor'] += 1
        print(f"  warning (no clipboard-btn.js tag, loader not added): {path}")
    else:
        loaders.add(os.path.normpath(os.path.join(os.path.dirname(path), prefix, 'assets', 'js', 'format-loader.js')))

    if new != text:
        stats['bytes_saved'] += len(text) - len(new)
        if already:
            stats['tag_added'] += 1
        if not dry_run:
            with open(path, 'wb') as f:
                f.write(new)


def slim_tree(roots, dry_run=False, log=print):
    stats = dict(converted=0, already=0, tag_added=0, skip_blocks=0,
                 skip_nosrc=0, skip_noanchor=0, bytes_saved=0, loaders_written=0)
    loaders = set()
    for root in roots:
        for d, dirs, files in os.walk(root):
            dirs[:] = [x for x in dirs if x != '.git']
            for name in files:
                if name.endswith(SUFFIXES):
                    slim_page(os.path.join(d, name), dry_run, stats, loaders)

    for loader in sorted(loaders):
        if not os.path.isfile(loader):
            stats['loaders_written'] += 1
            log(f"  add loader: {loader}")
            if not dry_run:
                os.makedirs(os.path.dirname(loader), exist_ok=True)
                with open(loader, 'w', encoding='utf-8', newline='\n') as f:
                    f.write(LOADER_JS)

    log(f"{'[dry run] ' if dry_run else ''}converted {stats['converted']} pages, "
        f"{stats['already']} already converted ({stats['tag_added']} given a loader tag), "
        f"{stats['loaders_written']} loader files added, "
        f"skipped {stats['skip_blocks'] + stats['skip_nosrc']}, "
        f"saved {stats['bytes_saved'] / 1048576:.0f} MB")
    return stats


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('dirs', nargs='+', help='folders to process (e.g. trust or trust/v1.7.2)')
    ap.add_argument('--dry-run', action='store_true', help='report only, write nothing')
    args = ap.parse_args()
    for d in args.dirs:
        if not os.path.isdir(d):
            sys.exit(f"not a directory: {d}")
    slim_tree(args.dirs, args.dry_run)


if __name__ == '__main__':
    main()
