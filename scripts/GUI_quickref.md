# 🎯 GUI Quick Command Reference

## Most Common Commands

### Basic Launch
```bash
# Just open the GUI
python ig_publisher_gui.py

# GUI with specific IG folder
python ig_publisher_gui.py --ig-folder hiv

# GUI from main script
python ig_publisher.py --gui
```

### Pre-filled GUI
```bash
# Fill in all the fields
python ig_publisher_gui.py \
  --ig-folder hiv \
  --push \
  --github-token $GITHUB_TOKEN
```

### Auto-Build
```bash
# Open GUI and start building immediately
python ig_publisher_gui.py --ig-folder hiv --auto-build
```

### No GUI (Headless)
```bash
# Run without showing GUI window
python ig_publisher_gui.py --ig-folder hiv --no-gui
```

## Essential Arguments Only

| What You Want | Command |
|--------------|---------|
| Open GUI | `python ig_publisher_gui.py` |
| Set IG folder | `--ig-folder hiv` |
| Auto-start build | `--auto-build` |
| Enable GitHub push | `--push` |
| Run without GUI | `--no-gui` |
| Debug mode | `--debug` |
| Dark theme | `--theme dark` |
| Save log | `--log-file build.log` |

## Real-World Examples

### 1. Developer Testing
```bash
python ig_publisher_gui.py --ig-folder hiv --debug
```

### 2. CI/CD Pipeline
```bash
python ig_publisher_gui.py \
  --ig-folder hiv \
  --no-gui \
  --push \
  --log-file build.log
```

### 3. Quick Build with GUI
```bash
python ig_publisher_gui.py --ig-folder hiv --auto-build
```

### 4. Full Automation
```bash
export GITHUB_TOKEN=ghp_xxxxx
python ig_publisher_gui.py \
  --ig-folder hiv \
  --auto-build \
  --push \
  --minimized
```

## Config File Shortcut

Save your settings once:
```bash
# Save config
python ig_publisher_gui.py \
  --ig-folder hiv \
  --webroot-repo WHO/smart-html \
  --save-config my-settings.json

# Use saved config
python ig_publisher_gui.py --config my-settings.json
```

## Windows Users

Create `ig-gui.bat`:
```batch
@echo off
python ig_publisher_gui.py %*
```

Then use:
```
ig-gui --ig-folder hiv
```

## Mac/Linux Users

Add to `~/.bashrc` or `~/.zshrc`:
```bash
alias ig-gui='python3 ~/scripts/ig_publisher_gui.py'
```

Then use:
```bash
ig-gui --ig-folder hiv
```

## Environment Variables

Instead of command line args:
```bash
export IG_FOLDER=hiv
export GITHUB_TOKEN=ghp_xxxxx
python ig_publisher_gui.py  # Will use env vars
```

## That's It! 🚀

90% of the time you'll just use:
```bash
# Open GUI
python ig_publisher_gui.py

# Or with folder
python ig_publisher_gui.py --ig-folder hiv

# Or auto-build
python ig_publisher_gui.py --ig-folder hiv --auto-build
```