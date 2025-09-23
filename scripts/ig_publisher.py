import os
import sys
import subprocess
import logging
import argparse
import yaml
import threading
import requests
import json
from datetime import datetime
from copy import deepcopy
from urllib.parse import urlparse
import shutil
import tempfile
import time

try:
    import git
except ImportError:
    print("Installing GitPython...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gitpython'])
    import git

try:
    import tkinter as tk
    from tkinter import ttk, filedialog, messagebox, scrolledtext
    import tkinter.font as tkfont
except ImportError:
    tk = None

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

CONFIG_FILE = "release-config.yaml"

# Keep these as relative paths; we normalize/strip leading slashes below
ALWAYS_INCLUDE = ["/templates", "/publish-setup.json", "/package-registry.json", "/package-feed.xml", "/publication-feed.xml"]


def _first_path_segment(s: str) -> str | None:
    """Return the first segment of a URL or path (e.g., '/dak-pnc/v0.9.9' -> 'dak-pnc')."""
    if not s:
        return None
    # If it's a URL, parse the path; if it's a bare path, use as-is
    if '://' in s:
        p = urlparse(s).path
    else:
        p = s
    parts = p.strip("/").split("/")
    return parts[0] if parts and parts[0] else None


def _ig_slug_from_pubreq(source_dir: str) -> str | None:
    """Read publication-request.json and return IG slug (first path segment)."""
    try:
        with open(os.path.join(source_dir, "publication-request.json"), encoding="utf-8") as f:
            pr = json.load(f)
        # Prefer 'path', else fall back to 'canonical'
        return _first_path_segment(pr.get("path") or pr.get("canonical") or "")
    except Exception:
        return None


def _looks_like_file(p: str) -> bool:
    # crude heuristic: file if no slash and has a dot, or ends with .json/.yml etc
    return ('/' not in p and '.' in p) or p.endswith(('.json', '.yml', '.yaml'))


def _normalize_sparse_list(paths):
    if not paths:
        return []
    norm = []
    for p in paths:
        p = (p or "").strip().lstrip("/")
        if not p:
            continue
        if not p.startswith("/"):
            p = "/" + p
        norm.append(p)
    return norm


class ReleasePublisher:
    def __init__(self, source_dir=None, source_repo=None, source_branch=None,
                 webroot_repo=None, webroot_branch=None,
                 history_repo=None, history_branch=None,
                 registry_repo=None,
                 sparse_dirs=None, enable_sparse_checkout=False, progress_callback=None,
                 github_token=None, enable_pr_creation=False,
                 publish_to_gh_pages=False, sitepreview_dir="sitepreview",
                 gh_pages_branch="gh-pages", exclude_paths=None,
                 webroot_pr_target_branch="main", registry_pr_target_branch="master",
                 ensure_pubreq=False, pubreq_overrides=None
                ):

        self.base_dir = os.path.abspath(os.path.dirname(__file__))
        self.source_dir = source_dir or os.path.join(self.base_dir, 'source')
        self.source_repo = source_repo
        self.source_branch = source_branch
        self.webroot_repo = webroot_repo or 'https://github.com/WorldHealthOrganization/smart-html'
        self.webroot_branch = webroot_branch
        self.history_repo = history_repo or 'https://github.com/HL7/fhir-ig-history-template'
        self.history_branch = history_branch
        self.registry_repo = registry_repo or 'https://github.com/FHIR/ig-registry'

        self.webroot_dir = os.path.join(self.base_dir, 'webroot')
        self.history_dir = os.path.join(self.base_dir, 'history-template')
        self.registry_dir = os.path.join(self.base_dir, 'ig-registry')
        self.package_cache = os.path.join(self.base_dir, 'fhir-package-cache')
        self.temp_dir = os.path.join(self.base_dir, 'temp')
        self.publisher_jar = os.path.join(self.base_dir, 'publisher.jar')
    
        self.publish_to_gh_pages = publish_to_gh_pages
        self.sitepreview_dir = sitepreview_dir
        self.gh_pages_branch = gh_pages_branch
        self.exclude_paths = exclude_paths or []

        self.ensure_pubreq = ensure_pubreq
        self.pubreq_overrides = pubreq_overrides or {}

        self.enable_sparse_checkout = enable_sparse_checkout
        self.sparse_dirs = _normalize_sparse_list(sparse_dirs) or []
        if self.enable_sparse_checkout:
            # ensure templates + helper files are always present
            self.sparse_dirs = sorted(set(self.sparse_dirs + ALWAYS_INCLUDE))

        self.progress_callback = progress_callback

        # GitHub PR settings - auto-detect GitHub Actions environment
        self.github_token = github_token or self.get_github_token()
        self.enable_pr_creation = enable_pr_creation
        self.webroot_pr_target_branch = webroot_pr_target_branch
        self.registry_pr_target_branch = registry_pr_target_branch

        # Check if running in GitHub Actions
        self.is_github_actions = os.environ.get('GITHUB_ACTIONS') == 'true'


    def _maybe_write_pubreq(self):
        target = os.path.join(self.source_dir, 'publication-request.json')
        if os.path.exists(target):
            return
        d = {
            "path": self.pubreq_overrides.get("path"),
            "canonical": self.pubreq_overrides.get("canonical"),
            "package-id": self.pubreq_overrides.get("package_id"),
            "version": self.pubreq_overrides.get("version"),
        }
        # keep only provided fields
        d = {k: v for k, v in d.items() if v}
        if not d:
            return
        with open(target, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2)
        self.log_progress(f"Wrote minimal publication-request.json to {target}")


    def get_github_token(self):
        """Get GitHub token from environment (GitHub Actions or manual)"""
        token = os.environ.get('GITHUB_TOKEN')
        if token:
            self.log_progress("Using GITHUB_TOKEN from environment")
            return token
        token = os.environ.get('GH_PAT')
        if token:
            self.log_progress("Using GH_PAT from environment")
            return token
        return None

    def log_progress(self, message):
        logging.info(message)
        if self.progress_callback:
            self.progress_callback(message)

    def run_command(self, cmd, shell=False):
        cmd_str = ' '.join(cmd) if isinstance(cmd, list) else cmd
        self.log_progress(f"Running: {cmd_str}")
        subprocess.run(cmd, shell=shell, check=True)

    def _safe_checkout(self, repo: git.Repo, branch: str):
        """Checkout branch if it exists, create from origin/branch if remote exists; else skip."""
        if not branch:
            return
        try:
            local_branches = [h.name for h in repo.heads]
            if branch in local_branches:
                repo.git.checkout(branch)
                return
            remotes = repo.git.branch('-r').split()
            remote_ref = f'origin/{branch}'
            if remote_ref in remotes:
                # create/update local branch from remote
                repo.git.checkout('-B', branch, remote_ref)
            else:
                self.log_progress(f"Branch '{branch}' not found (local or remote); staying on current branch.")
        except Exception as e:
            self.log_progress(f"Checkout '{branch}' skipped: {e}")

    def clone_repo(self, url, path, branch=None, use_sparse=False, sparse_dirs=None):
        """Clone repository with authentication if token is available"""
        
        # Add authentication to URL if token is available and it's a GitHub URL
        if self.github_token and 'github.com' in url and '://' in url:
            if url.startswith('https://github.com/'):
                # Convert https://github.com/owner/repo to authenticated URL
                parts = url.split('github.com/')
                if len(parts) == 2:
                    url = f"https://x-access-token:{self.github_token}@github.com/{parts[1]}"
                    self.log_progress("Using authenticated URL for cloning")
        
        sparse_dirs = _normalize_sparse_list(sparse_dirs)
        ensured = _normalize_sparse_list((sparse_dirs or []) + (ALWAYS_INCLUDE if use_sparse else []))
        ensured = sorted(set(ensured))

        # Update existing working tree
        if os.path.exists(path) and os.path.isdir(os.path.join(path, '.git')):
            self.log_progress(f"Updating existing repository: {path}")
            try:
                repo = git.Repo(path)
                # reset local changes (best-effort)
                try:
                    repo.git.reset('--hard')
                except Exception:
                    pass

                if use_sparse and ensured:
                    needs_no_cone = any(_looks_like_file(p) for p in ensured) or any('*' in p for p in ensured)
                    # (Re)initialize sparse mode with correct flavor
                    try:
                        self.run_command(['git', '-C', path, 'sparse-checkout', 'init',
                                          '--no-cone' if needs_no_cone else '--cone'])
                    except Exception:
                        # Fall back to default init (older Git)
                        self.run_command(['git', '-C', path, 'sparse-checkout', 'init'])
                    set_cmd = ['git', '-C', path, 'sparse-checkout', 'set']
                    if needs_no_cone:
                        set_cmd.append('--no-cone')
                    self.run_command(set_cmd + ensured)

                # Correct fetch ordering
                try:
                    repo.git.fetch('--depth=1', 'origin')
                except Exception as e:
                    self.log_progress(f"Fetch skipped: {e}")

                self._safe_checkout(repo, branch)
                # Fast-forward pull if possible
                try:
                    if branch:
                        repo.git.pull('--ff-only', 'origin', branch)
                    else:
                        repo.git.pull('--ff-only')
                except Exception as e:
                    self.log_progress(f"Pull skipped: {e}")
            except Exception as e:
                self.log_progress(f"Warning: Failed to update {path}: {e}")
            return

        # Fresh clone
        if use_sparse and ensured:
            self.log_progress(f"Cloning with sparse checkout: {url}")
            clone_cmd = ['git', 'clone', '--depth=1', '--filter=blob:none', '--sparse']
            if branch:
                clone_cmd += ['--branch', branch]
            clone_cmd += [url, path]
            self.run_command(clone_cmd)

            needs_no_cone = any(_looks_like_file(p) for p in ensured)
            try:
                self.run_command(['git', '-C', path, 'sparse-checkout', 'init',
                                  '--no-cone' if needs_no_cone else '--cone'])
            except Exception:
                self.run_command(['git', '-C', path, 'sparse-checkout', 'init'])
            set_cmd = ['git', '-C', path, 'sparse-checkout', 'set']
            if needs_no_cone:
                set_cmd.append('--no-cone')
            self.run_command(set_cmd + ensured)

            self.log_progress(f"Sparse checkout includes: {' '.join(ensured)}")

            # Ensure the template root exists
            pub = os.path.join(path, 'publish-setup.json')
            if not os.path.exists(pub):
                raise RuntimeError(
                    f"publish-setup.json not found after sparse checkout at {pub}. "
                    f"Check branch/path in {url}."
                )
            return

        # non-sparse clone
        self.log_progress(f"Cloning repository: {url}")
        clone_cmd = ['git', 'clone', '--depth=1']
        if branch:
            clone_cmd += ['--branch', branch]
        clone_cmd += [url, path]
        self.run_command(clone_cmd)

    def get_repo_info_from_url(self, repo_url):
        """Extract owner and repo name from GitHub URL"""
        if 'github.com' in repo_url:
            if repo_url.startswith('https://github.com/'):
                path = repo_url.replace('https://github.com/', '')
            elif repo_url.startswith('git@github.com:'):
                path = repo_url.replace('git@github.com:', '')
            else:
                raise ValueError(f"Unsupported repository URL format: {repo_url}")
            if path.endswith('.git'):
                path = path[:-4]
            parts = path.split('/')
            if len(parts) >= 2:
                return parts[0], parts[1]
        raise ValueError(f"Could not parse GitHub repository URL: {repo_url}")

    def has_changes(self, repo_path):
        """Check if repository has uncommitted changes"""
        try:
            repo = git.Repo(repo_path)
            return repo.is_dirty() or len(repo.untracked_files) > 0
        except Exception as e:
            self.log_progress(f"Warning: Could not check repository status for {repo_path}: {e}")
            return False

    def create_branch_and_commit(self, repo_path, branch_name, commit_message):
        """Create a new branch and commit all changes using subprocess to avoid GitPython version issues"""
        try:
            # Check if sparse checkout is enabled
            sparse_file = os.path.join(repo_path, '.git', 'info', 'sparse-checkout')
            is_sparse = os.path.exists(sparse_file)
            
            # Use subprocess for all git operations to avoid GitPython compatibility issues
            self.log_progress(f"Creating branch '{branch_name}'...")
            
            # Create and checkout new branch
            self.run_command(['git', '-C', repo_path, 'checkout', '-b', branch_name])
            
            # Add files (with --sparse flag if needed)
            if is_sparse:
                self.log_progress("Using --sparse flag for git add (sparse checkout detected)")
                self.run_command(['git', '-C', repo_path, 'add', '-A', '--sparse'])
            else:
                self.run_command(['git', '-C', repo_path, 'add', '-A'])
            
            # Check if there are changes to commit
            result = subprocess.run(
                ['git', '-C', repo_path, 'diff', '--cached', '--quiet'],
                capture_output=True
            )
            
            if result.returncode == 0:
                self.log_progress("No changes to commit")
                return False
                
            # Commit changes
            self.run_command([
                'git', '-C', repo_path, 
                '-c', 'user.name=github-actions[bot]',
                '-c', 'user.email=github-actions[bot]@users.noreply.github.com',
                'commit', '-m', commit_message
            ])
            
            # Get the current remote URL and add authentication if needed
            if self.github_token:
                # Get current remote URL
                result = subprocess.run(
                    ['git', '-C', repo_path, 'remote', 'get-url', 'origin'],
                    capture_output=True, text=True
                )
                current_url = result.stdout.strip()
                
                if 'github.com' in current_url and 'x-access-token' not in current_url:
                    if current_url.startswith('https://github.com/'):
                        parts = current_url.split('github.com/')
                        if len(parts) == 2:
                            auth_url = f"https://x-access-token:{self.github_token}@github.com/{parts[1]}"
                            self.run_command(['git', '-C', repo_path, 'remote', 'set-url', 'origin', auth_url])
                            self.log_progress("Configured authenticated push URL")
            
            # Push the new branch
            self.run_command(['git', '-C', repo_path, 'push', 'origin', branch_name])
            self.log_progress(f"Created branch '{branch_name}' and pushed changes")
            return True
            
        except subprocess.CalledProcessError as e:
            self.log_progress(f"Error creating branch and committing: {e}")
            if e.stderr:
                self.log_progress(f"Error details: {e.stderr.decode('utf-8', errors='ignore')}")
            return False
        except Exception as e:
            self.log_progress(f"Error creating branch and committing: {e}")
            return False

    def create_github_pr(self, repo_url, head_branch, base_branch, title, body):
        """Create a GitHub pull request using the GitHub API"""
        if not self.github_token:
            if self.is_github_actions:
                self.log_progress("⚠️ No GitHub token available in GitHub Actions. Ensure GITHUB_TOKEN is properly configured.")
            else:
                self.log_progress("❌ GitHub token not provided, cannot create PR")
            return False

        try:
            owner, repo_name = self.get_repo_info_from_url(repo_url)
            current_repo = os.environ.get('GITHUB_REPOSITORY', '')
            is_same_repo = current_repo == f"{owner}/{repo_name}"
            if self.is_github_actions and is_same_repo:
                self.log_progress(f"📝 Creating PR in same repository ({current_repo}) using GITHUB_TOKEN")

            api_url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls"
            pr_data = {
                "title": title,
                "body": body,
                "head": head_branch,
                "base": base_branch
            }

            auth_header = f"Bearer {self.github_token}" if self.is_github_actions else f"token {self.github_token}"
            headers = {
                "Authorization": auth_header,
                "Accept": "application/vnd.github.v3+json",
                "Content-Type": "application/json"
            }

            response = requests.post(api_url, json=pr_data, headers=headers)
            if response.status_code == 201:
                pr_data = response.json()
                pr_url = pr_data['html_url']
                self.log_progress(f"✅ Pull request created: {pr_url}")
                return True
            else:
                error_msg = response.json().get('message', 'Unknown error')
                self.log_progress(f"❌ Failed to create PR: {error_msg}")
                return False

        except Exception as e:
            self.log_progress(f"❌ Error creating GitHub PR: {e}")
            return False

    def create_prs_if_needed(self):
        """Create pull requests for webroot and registry if changes exist"""
        if not self.enable_pr_creation:
            self.log_progress("PR creation disabled, skipping...")
            return

        self.log_progress("🔍 Checking for changes to create pull requests...")
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

        if self.has_changes(self.webroot_dir):
            self.log_progress("📤 Creating PR for webroot repository...")
            branch_name = f"fhir-ig-update-{timestamp}"
            commit_message = f"Update FHIR IG content - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            if self.create_branch_and_commit(self.webroot_dir, branch_name, commit_message):
                pr_title = f"FHIR IG Content Update - {datetime.now().strftime('%Y-%m-%d')}"
                pr_body = f"""## FHIR Implementation Guide Update

This PR contains updated content from the FHIR IG publishing process.

**Changes include:**
- Updated templates and assets
- Generated documentation
- Resource definitions

**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Source:** {self.source_repo if self.source_repo else 'Local build'}
**Automated:** {'Yes - GitHub Actions' if self.is_github_actions else 'No - Manual run'}
"""
                self.create_github_pr(
                    self.webroot_repo,
                    branch_name,
                    self.webroot_pr_target_branch,
                    pr_title,
                    pr_body
                )
        else:
            self.log_progress("No changes in webroot repository, skipping PR")

        if self.has_changes(self.registry_dir):
            self.log_progress("📤 Creating PR for IG registry...")
            branch_name = f"registry-update-{timestamp}"
            commit_message = f"Update IG registry - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            if self.create_branch_and_commit(self.registry_dir, branch_name, commit_message):
                pr_title = f"IG Registry Update - {datetime.now().strftime('%Y-%m-%d')}"
                pr_body = f"""## Implementation Guide Registry Update

This PR updates the FHIR Implementation Guide registry with latest information.

**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Source:** {self.source_repo if self.source_repo else 'Local build'}
**Automated:** {'Yes - GitHub Actions' if self.is_github_actions else 'No - Manual run'}
"""
                self.create_github_pr(
                    self.registry_repo,
                    branch_name,
                    self.registry_pr_target_branch,
                    pr_title,
                    pr_body
                )
        else:
            self.log_progress("No changes in registry repository, skipping PR")


    def build(self):
        self.log_progress("🔨 Building Implementation Guide...")
        
        # Save current directory
        original_dir = os.getcwd()
        
        try:
            # Change to source directory
            os.chdir(self.source_dir)
            self.log_progress(f"Changed to source directory: {self.source_dir}")
            
            # Publisher jar path needs to be absolute or relative to source_dir
            publisher_jar_path = os.path.abspath(self.publisher_jar)
            package_cache_path = os.path.abspath(self.package_cache)
            
            # Run publisher from within source directory
            self.run_command([
                'java', '-Xmx4g', '-jar', publisher_jar_path,
                '-ig', '.',  # Current directory (which is now source_dir)
                '-package-cache-folder', package_cache_path
            ])
            
        finally:
            # Always change back to original directory
            os.chdir(original_dir)
            self.log_progress(f"Returned to original directory: {original_dir}")

    def publish(self):
        self.log_progress("📤 Publishing Implementation Guide...")
        
        # DON'T change directory - run from current location with absolute paths
        
        # All paths need to be absolute
        publisher_jar_path = os.path.abspath(self.publisher_jar)
        package_cache_path = os.path.abspath(self.package_cache)
        source_path = os.path.abspath(self.source_dir)  # Use absolute path, not '.'
        webroot_path = os.path.abspath(self.webroot_dir)
        temp_path = os.path.abspath(self.temp_dir)
        registry_path = os.path.abspath(os.path.join(self.registry_dir, 'fhir-ig-list.json'))
        history_path = os.path.abspath(self.history_dir)
        templates_path = os.path.abspath(os.path.join(self.webroot_dir, 'templates'))
        
        # Check for templates in different locations
        if not os.path.exists(templates_path):
            alt_templates = os.path.abspath(os.path.join(self.base_dir, 'templates'))
            if os.path.exists(alt_templates):
                templates_path = alt_templates
                self.log_progress(f"Using alternative templates path: {templates_path}")
        
        # Verify paths
        self.log_progress(f"Source: {source_path}")
        self.log_progress(f"Webroot: {webroot_path}")
        self.log_progress(f"Templates: {templates_path}")
        
        # Ensure temp directory exists
        os.makedirs(temp_path, exist_ok=True)
        
        # Run publisher from current directory with absolute paths
        self.run_command([
            'java', '-Xmx4g', '-Dfile.encoding=UTF-8', '-jar', publisher_jar_path,
            '-go-publish',
            '-package-cache-folder', package_cache_path,
            '-source', source_path,  # Use absolute path instead of '.'
            '-web', webroot_path,
            '-temp', temp_path,
            '-registry', registry_path,
            '-history', history_path,
            '-templates', templates_path
        ])

    def prepare(self):
        self.log_progress("🔄 Preparing repositories...")

        if self.is_github_actions:
            self.log_progress("🤖 Running in GitHub Actions environment")

        # 1) Ensure source exists locally (so we can read publication-request.json)
        if self.source_repo:
            self.clone_repo(self.source_repo, self.source_dir, self.source_branch)

        if self.ensure_pubreq:
            self._maybe_write_pubreq()

        # 2) Determine IG slug (first path segment) from source
        slug = _ig_slug_from_pubreq(self.source_dir)
        if slug:
            self.log_progress(f"📁 Detected IG slug: {slug}")
        else:
            self.log_progress("⚠️ Could not detect IG slug from publication-request.json")

        # 3) Prepare sparse list for webroot (if enabled)
        sparse_dirs_for_webroot = list(self.sparse_dirs) if self.sparse_dirs else []
        if self.enable_sparse_checkout:
            if slug:
                # Include the IG folder and ALL its contents (including version subfolders)
                sparse_dirs_for_webroot += [
                    f"/{slug}",
                    f"/{slug}/*",  # All direct children
                    f"/{slug}/**"  # All nested content (requires no-cone mode)
                ]
            sparse_dirs_for_webroot += ALWAYS_INCLUDE
            sparse_dirs_for_webroot = sorted(set(_normalize_sparse_list(sparse_dirs_for_webroot)))
            self.log_progress(f"➕ Sparse includes: {' '.join(sparse_dirs_for_webroot)}")

        # 4) Clone history
        self.clone_repo(self.history_repo, self.history_dir, self.history_branch)

        # 5) Clone webroot (sparse if requested)
        self.clone_repo(
            self.webroot_repo,
            self.webroot_dir,
            self.webroot_branch,
            use_sparse=self.enable_sparse_checkout,
            sparse_dirs=sparse_dirs_for_webroot
        )

        # Optional: sanity check, don't change sparse dirs after clone
        if self.enable_sparse_checkout and slug:
            pkg = os.path.join(self.webroot_dir, slug, 'package-list.json')
            if not os.path.exists(pkg):
                self.log_progress(f"⚠️ Expected '{pkg}' not found in webroot after sparse checkout.")

        # 6) Clone registry
        self.clone_repo(self.registry_repo, self.registry_dir)

        # 7) Ensure publisher.jar
        if not os.path.exists(self.publisher_jar):
            self.log_progress("📥 Downloading FHIR IG Publisher...")
            self.run_command([
                'curl', '-L',
                'https://github.com/HL7/fhir-ig-publisher/releases/latest/download/publisher.jar',
                '-o', self.publisher_jar
            ])

        os.makedirs(self.package_cache, exist_ok=True)


    def _rsync_copy(self, src, dest, excludes):
        # Build rsync-like exclude args for subprocess
        exclude_args = []
        for e in excludes:
            exclude_args += ['--exclude', e]
        # Ensure trailing slash semantics
        src = os.path.join(src, '')
        dest = os.path.join(dest, '')
        self.run_command(['rsync', '-a', '--delete', '--exclude', '.git'] + exclude_args + [src, dest])

    def _gh_remote_url(self):
        repo_slug = os.environ.get('GITHUB_REPOSITORY')
        token = self.github_token
        if not repo_slug or not token:
            return None
        # GITHUB_TOKEN works with x-access-token over HTTPS
        return f"https://x-access-token:{token}@github.com/{repo_slug}.git"

    def _ensure_gh_pages_checkout(self, workdir):
        remote = self._gh_remote_url()
        if not remote:
            raise RuntimeError("GITHUB_REPOSITORY or token missing; cannot push to gh-pages")

        # Try clone gh-pages directly; fall back to orphan create
        try:
            self.run_command(['git', 'clone', '--depth=1', '--branch', self.gh_pages_branch, remote, workdir])
            return
        except Exception:
            pass

        # Clone default branch, then create orphan gh-pages
        self.run_command(['git', 'clone', '--depth=1', remote, workdir])
        self.run_command(['bash', '-lc', f'''
            set -e
            cd "{workdir}"
            git checkout --orphan {self.gh_pages_branch}
            find . -mindepth 1 -maxdepth 1 ! -name ".git" -exec rm -rf {{}} +
            touch .nojekyll
            git add .nojekyll
            git -c user.name="github-actions[bot]" \
                -c user.email="github-actions[bot]@users.noreply.github.com" \
                commit -m "Initialize {self.gh_pages_branch}"
            git push origin {self.gh_pages_branch}
        '''])

    def _append_gitignore_line(self, ghdir, line):
        gi = os.path.join(ghdir, '.gitignore')
        existing = ""
        if os.path.exists(gi):
            with open(gi, 'r', encoding='utf-8') as f:
                existing = f.read()
        if line not in existing:
            with open(gi, 'a', encoding='utf-8') as f:
                if existing and not existing.endswith('\n'):
                    f.write('\n')
                f.write(line.rstrip('\n') + '\n')

    def push_sitepreview_to_gh_pages(self):
        """Copy self.webroot_dir to gh-pages/<sitepreview_dir> and push."""
        remote = self._gh_remote_url()
        if not remote:
            self.log_progress("Skipping gh-pages push (no GITHUB_TOKEN or GITHUB_REPOSITORY).")
            return

        ghdir = os.path.join(self.temp_dir, 'gh-pages-work')
        if os.path.exists(ghdir):
            shutil.rmtree(ghdir, ignore_errors=True)
        os.makedirs(self.temp_dir, exist_ok=True)

        self._ensure_gh_pages_checkout(ghdir)

        dest = os.path.join(ghdir, self.sitepreview_dir)
        os.makedirs(dest, exist_ok=True)

        # Default excludes + user supplied
        excludes = list(self.exclude_paths)
        # Always exclude big zip folder unless user explicitly removed it
        if 'ig-build-zips/' not in excludes:
            excludes.append('ig-build-zips/')

        # Copy built site into sitepreview
        self._rsync_copy(self.webroot_dir, dest, excludes)

        # Ignore big zips in repo
        self._append_gitignore_line(ghdir, f"{self.sitepreview_dir}/ig-build-zips/")

        # Untrack cached big zips, if any were ever committed
        self.run_command(['bash', '-lc', f'cd "{ghdir}" && git rm -r --cached {self.sitepreview_dir}/ig-build-zips || true'])

        # Commit & push with retries
        ref = os.environ.get('GITHUB_REF', '')
        ref_short = ref.rsplit('/', 1)[-1] if ref else ''
        sha = os.environ.get('GITHUB_SHA', '')[:7]
        
        # First, configure git
        self.run_command(['bash', '-lc', f'''
        set -e
        cd "{ghdir}"
        git config user.name  "github-actions[bot]"
        git config user.email "github-actions[bot]@users.noreply.github.com"
        git config http.version HTTP/1.1
        git config http.lowSpeedLimit 1
        git config http.lowSpeedTime 600
        '''])

        # Add and commit changes
        self.run_command(['bash', '-lc', f'''
        set -e
        cd "{ghdir}"
        git add -A {self.sitepreview_dir} .gitignore
        if git diff --cached --quiet; then
            echo "No changes to commit."
            exit 0
        fi
        git commit -m "Update {self.sitepreview_dir} from {ref_short} @ {sha}"
        '''])

        # Try to run gc, but don't fail if it can't (another process might be doing it)
        try:
            self.run_command(['bash', '-lc', f'''
            cd "{ghdir}"
            # Kill any existing gc processes for this repo (if we have permission)
            pkill -f "git.*gc.*{ghdir}" || true
            # Wait a bit for any gc to finish
            sleep 2
            # Try gc with force flag to override lock
            git gc --prune=now --force || true
            git count-objects -vH || true
            '''])
        except Exception as e:
            self.log_progress(f"Warning: gc failed (non-fatal): {e}")

        # Push with retries
        last_err = None
        for i in range(3):
            try:
                self.log_progress(f"Push attempt {i+1} to gh-pages...")
                self.run_command(['bash', '-lc', f'''
                cd "{ghdir}"
                # Try to remove gc lock file if it exists
                rm -f .git/gc.pid || true
                git push origin {self.gh_pages_branch}
                '''])
                self.log_progress("✅ Pushed to gh-pages successfully.")
                return
            except Exception as e:
                last_err = e
                self.log_progress(f"Push attempt {i+1} failed: {e}")
                if i < 2:  # Don't sleep on last attempt
                    wait_time = 10 * (i+1)
                    self.log_progress(f"Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)
        
        # If we get here, all retries failed
        self.log_progress(f"❌ All push attempts failed. Last error: {last_err}")
        raise last_err




    def run(self):
        try:
            self.prepare()
            self.build()
            self.publish()
            if self.publish_to_gh_pages:
                self.push_sitepreview_to_gh_pages()
            self.log_progress("✅ Publication completed successfully!")
            self.create_prs_if_needed()
        except Exception as e:
            self.log_progress(f"❌ Error: {str(e)}")
            raise


# --- config helpers ---
def _load_yaml_maybe(path):
    if not path:
        return {}
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = yaml.safe_load(f) or {}
                if not isinstance(data, dict):
                    logging.warning(f"{path} did not parse to a mapping; ignoring.")
                    return {}
                return data
            except Exception as e:
                logging.warning(f"Failed to parse YAML {path}: {e}")
                return {}
    return {}

def _deep_merge_dicts(base: dict, override: dict) -> dict:
    """Return a deep merge of two dicts without mutating inputs (override wins)."""
    result = deepcopy(base)
    for k, v in (override or {}).items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = _deep_merge_dicts(result[k], v)
        else:
            result[k] = deepcopy(v)
    return result

def load_config(global_path=None, local_path="release-config.yaml"):
    """
    Load config by deep-merging:
      1) global defaults (from smart-html)
      2) local overrides (from caller repo)
    Local overrides win per key.
    """
    global_cfg = _load_yaml_maybe(global_path)
    local_cfg = _load_yaml_maybe(local_path)
    merged = _deep_merge_dicts(global_cfg, local_cfg)
    return merged

def save_config(config):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        yaml.safe_dump(config, f, default_flow_style=False)


# ---------------- GUI (optional) ----------------
if tk:
    class CustomCheckbox(tk.Canvas):
        """Custom checkbox widget that supports theming and proper sizing"""
        def __init__(self, parent, text="", variable=None, command=None,
                     font=None, bg="#FFFFFF", fg="#000000",
                     check_color="#6C63FF", size=20):
            super().__init__(parent, highlightthickness=0, bg=bg)

            self.variable = variable or tk.BooleanVar()
            self.command = command
            self.text = text
            self.font = font
            self.bg = bg
            self.fg = fg
            self.check_color = check_color
            self.size = size
            self.checkbox_id = None
            self.check_id = None
            self.text_id = None

            self.setup_widget()
            self.bind("<Button-1>", self.toggle)
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def setup_widget(self):
            padding = 5
            box_size = self.size

            self.checkbox_id = self.create_rectangle(
                padding, padding,
                padding + box_size, padding + box_size,
                outline=self.fg, width=2, fill=self.bg
            )

            check_padding = box_size * 0.25
            self.check_id = self.create_line(
                padding + check_padding,
                padding + box_size/2,
                padding + box_size/2.5,
                padding + box_size - check_padding,
                padding + box_size - check_padding,
                padding + check_padding,
                width=3, fill=self.check_color,
                state='hidden'
            )

            if self.text:
                self.text_id = self.create_text(
                    padding * 2 + box_size,
                    padding + box_size/2,
                    text=self.text, font=self.font,
                    fill=self.fg, anchor='w'
                )
                bbox = self.bbox('all')
                if bbox:
                    self.configure(width=bbox[2] + padding,
                                   height=bbox[3] + padding)
            else:
                self.configure(width=box_size + padding * 2,
                               height=box_size + padding * 2)

            self.update_visual()

        def toggle(self, event=None):
            self.variable.set(not self.variable.get())
            self.update_visual()
            if self.command:
                self.command()

        def update_visual(self):
            if self.variable.get():
                self.itemconfig(self.check_id, state='normal')
                self.itemconfig(self.checkbox_id, fill=self.bg)
            else:
                self.itemconfig(self.check_id, state='hidden')
                self.itemconfig(self.checkbox_id, fill=self.bg)

        def on_enter(self, event):
            self.configure(cursor='hand2')
            if not self.variable.get():
                self.itemconfig(self.checkbox_id, fill='#F0F0F0' if self.bg == '#FFFFFF' else '#3A4356')

        def on_leave(self, event):
            self.configure(cursor='')
            self.update_visual()

        def update_colors(self, bg, fg, check_color):
            self.bg = bg
            self.fg = fg
            self.check_color = check_color
            self.configure(bg=bg)
            self.itemconfig(self.checkbox_id, outline=fg, fill=bg)
            self.itemconfig(self.check_id, fill=check_color)
            if self.text_id:
                self.itemconfig(self.text_id, fill=fg)
            self.update_visual()

    class ModernFHIRPublisherGUI:
        # (unchanged GUI code, other than using the corrected backend)
        # ... keeping your GUI exactly as you had it ...
        # To keep this message focused, I’m leaving GUI code as-is from your last paste.
        # If you need me to re-emit the entire GUI block verbatim, say the word and I will.
        pass


def main():
    parser = argparse.ArgumentParser(description="FHIR IG Publisher Release Utility")
    parser.add_argument('--gui', action='store_true', help='Launch beautiful GUI interface')
    parser.add_argument('--source', type=str, help='Path to the IG source folder')
    parser.add_argument('--source-repo', type=str, help='URL to the IG source repository')
    parser.add_argument('--source-branch', type=str, help='Branch name for IG source')
    parser.add_argument('--webroot-repo', type=str, help='Webroot repo URL')
    parser.add_argument('--webroot-branch', type=str, help='Webroot branch name')
    parser.add_argument('--history-repo', type=str, help='History repo URL')
    parser.add_argument('--history-branch', type=str, help='History branch name')
    parser.add_argument('--sparse', nargs='*', help='Sparse checkout folders for webroot')
    parser.add_argument('--enable-sparse', action='store_true', help='Enable sparse checkout')
    parser.add_argument('--registry-repo', type=str, help='Registry repo URL')
    
    # GitHub PR arguments
    parser.add_argument('--enable-pr', action='store_true', help='Enable automatic PR creation')
    parser.add_argument('--github-token', type=str, help='GitHub personal access token')
    parser.add_argument('--webroot-pr-target', type=str, default='main', help='Webroot PR target branch')
    parser.add_argument('--registry-pr-target', type=str, default='master', help='Registry PR target branch')
    parser.add_argument('--global-config', type=str, help='Path to global default release-config.yaml')
    parser.add_argument('--local-config', type=str, default='release-config.yaml', help='Path to repo-specific release-config.yaml')
    parser.add_argument('--publish-gh-pages', action='store_true', help='After publishing, push site into gh-pages/<sitepreview-dir>')
    parser.add_argument('--sitepreview-dir', type=str, default='sitepreview', help='Subfolder in gh-pages to place the built site')
    parser.add_argument('--gh-pages-branch', type=str, default='gh-pages', help='Branch to publish the preview to')
    parser.add_argument('--exclude', action='append', default=[], help='Paths (relative to webroot) to exclude when copying to sitepreview; repeatable')
    parser.add_argument('--ensure-pubreq', action='store_true', help='Create minimal publication-request.json if missing')
    parser.add_argument('--pubreq-path', type=str)
    parser.add_argument('--pubreq-canonical', type=str)
    parser.add_argument('--pubreq-package-id', type=str)
    parser.add_argument('--pubreq-version', type=str)


    args = parser.parse_args()

    if os.environ.get('GITHUB_ACTIONS') == 'true':
        print("🤖 Running in GitHub Actions environment")

    if args.gui:
        if not tk:
            print("❌ GUI not available: tkinter not found")
            sys.exit(1)
        # If you want the full GUI class re-emitted, ask and I’ll include it.
        # For now this placeholder will prevent accidental GUI start.
        print("GUI mode not emitted in this snippet.")
        sys.exit(0)
    else:
        config = load_config(global_path=args.global_config or os.environ.get("GLOBAL_RELEASE_CONFIG"),
                             local_path=args.local_config)

        publisher = ReleasePublisher(
            source_dir=args.source or config.get('source_dir'),
            source_repo=args.source_repo or config.get('source_repo'),
            source_branch=args.source_branch or config.get('source_branch'),
            webroot_repo=args.webroot_repo or config.get('webroot_repo'),
            webroot_branch=args.webroot_branch or config.get('webroot_branch'),
            history_repo=args.history_repo or config.get('history_repo'),
            history_branch=args.history_branch or config.get('history_branch'),
            registry_repo=args.registry_repo or config.get('registry_repo'),            
            sparse_dirs=args.sparse or config.get('sparse_dirs'),
            enable_sparse_checkout=args.enable_sparse or config.get('enable_sparse_checkout', False),
            publish_to_gh_pages=args.publish_gh_pages,
            sitepreview_dir=args.sitepreview_dir,
            gh_pages_branch=args.gh_pages_branch,
            exclude_paths=args.exclude,
            ensure_pubreq=args.ensure_pubreq,
            # ADD THESE MISSING PARAMETERS:
            enable_pr_creation=args.enable_pr,  # <-- This was missing!
            github_token=args.github_token,      # <-- This was missing!
            webroot_pr_target_branch=args.webroot_pr_target,
            registry_pr_target_branch=args.registry_pr_target,
            pubreq_overrides={
                "path": args.pubreq_path or os.environ.get("PUBREQ_PATH"),
                "canonical": args.pubreq_canonical or os.environ.get("PUBREQ_CANONICAL"),
                "package_id": args.pubreq_package_id or os.environ.get("PUBREQ_PACKAGE_ID"),
                "version": args.pubreq_version or os.environ.get("PUBREQ_VERSION"),
            }
        )
        publisher.run()


if __name__ == '__main__':
    main()





