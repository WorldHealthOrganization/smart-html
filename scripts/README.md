# FHIR IG Publisher

A Python-based FHIR Implementation Guide publisher that automates building, deployment, and PR creation with **zero Python dependencies** - uses only standard library!

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org)
[![Java](https://img.shields.io/badge/java-17%2B-orange)](https://adoptium.net/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## 🚀 Quick Start

### GitHub Actions (Most Common)

```yaml
name: Build IG

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - uses: actions/setup-java@v3
        with:
          java-version: '17'
          distribution: 'temurin'
      
      # No pip install needed! Just run:
      - name: Build IG
        run: python scripts/ig_publisher.py --ig-folder hiv
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./deploy
```

### Local Development

```bash
# Clone and run - no installation needed!
git clone https://github.com/your-org/your-ig-repo.git
cd your-ig-repo
python ig_publisher.py --ig-folder hiv
```

## 📋 Table of Contents

- [Features](#features)
- [GitHub Actions Usage](#github-actions-usage)
- [Installation](#installation)
- [Usage Options](#usage-options)
- [Command Line Reference](#command-line-reference)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)

## ✨ Features

- **Zero Python Dependencies** - Uses only standard library, no pip install needed
- **Sparse Checkout** - Clones only needed folders, saves 90% disk space
- **Auto-detection** - Reads `publication-request.json` automatically
- **PR Automation** - Creates PRs to webroot and registry repos
- **GUI Interface** - Optional graphical interface for local development
- **GitHub Actions Ready** - Designed for CI/CD pipelines
- **No Token Mode** - Build without GitHub authentication

## 🔧 GitHub Actions Usage

### Basic Build Pipeline

```yaml
name: Build and Deploy IG

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:
    inputs:
      ig_folder:
        description: 'IG folder (leave empty to auto-detect)'
        required: false
        type: string

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4
        with:
          fetch-depth: 1
      
      - name: Setup Build Environment
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Setup Java
        uses: actions/setup-java@v3
        with:
          java-version: '17'
          distribution: 'temurin'
      
      - name: Build IG
        run: |
          python scripts/ig_publisher.py \
            --ig-folder ${{ inputs.ig_folder }} \
            --work-dir . \
            --debug
      
      - name: Upload Build Artifacts
        uses: actions/upload-artifact@v4
        with:
          name: ig-build
          path: |
            deploy/
            release-assets/
          retention-days: 30
      
      - name: Deploy to GitHub Pages
        if: github.ref == 'refs/heads/main'
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./deploy
          destination_dir: ${{ inputs.ig_folder || 'site' }}
```

### Advanced Pipeline with PR Creation

```yaml
name: Build and Create PRs

on:
  release:
    types: [published]
  workflow_dispatch:

permissions:
  contents: write
  pull-requests: write
  pages: write

jobs:
  build-and-publish:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - uses: actions/setup-java@v3
        with:
          java-version: '17'
          distribution: 'temurin'
      
      # Build and create PRs (requires PAT token)
      - name: Build IG and Create PRs
        env:
          GITHUB_TOKEN: ${{ secrets.PAT_TOKEN }}  # Personal Access Token with repo access
        run: |
          python scripts/ig_publisher.py \
            --push \
            --debug
      
      # Deploy to Pages
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./deploy
      
      # Upload package to release
      - name: Upload Release Package
        if: github.event_name == 'release'
        uses: actions/upload-release-asset@v1
        with:
          upload_url: ${{ github.event.release.upload_url }}
          asset_path: ./release-assets/package.tgz
          asset_name: package.tgz
          asset_content_type: application/gzip
```

### Multi-IG Build Matrix

```yaml
name: Build Multiple IGs

on:
  workflow_dispatch:
    inputs:
      ig_selection:
        type: choice
        description: 'Which IGs to build'
        options:
          - hiv
          - tuberculosis
          - malaria
          - all

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        ig: ${{ fromJson(github.event.inputs.ig_selection == 'all' && '["hiv", "tuberculosis", "malaria"]' || format('["{0}"]', github.event.inputs.ig_selection)) }}
    
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
      - uses: actions/setup-java@v3
        with:
          java-version: '17'
      
      - name: Build ${{ matrix.ig }} IG
        run: python scripts/ig_publisher.py --ig-folder ${{ matrix.ig }}
      
      - name: Deploy ${{ matrix.ig }} to Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./deploy
          destination_dir: ${{ matrix.ig }}
```

### Scheduled Nightly Build

```yaml
name: Nightly Build

on:
  schedule:
    - cron: '0 2 * * *'  # 2 AM UTC daily
  workflow_dispatch:

jobs:
  nightly:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
      - uses: actions/setup-java@v3
        with:
          java-version: '17'
      
      - name: Run Nightly Build
        run: |
          python scripts/ig_publisher.py \
            --ig-folder hiv \
            --debug \
            --work-dir .
      
      - name: Notify on Failure
        if: failure()
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: 'Nightly IG Build Failed',
              body: `The nightly build failed. Check the [workflow run](${context.serverUrl}/${context.repo.owner}/${context.repo.repo}/actions/runs/${context.runId})`
            })
```

## 💻 Installation

### System Requirements

| Component | Version | Required | Check Command |
|-----------|---------|----------|---------------|
| Python | 3.8+ | ✅ Yes | `python --version` |
| Java | 17+ | ✅ Yes | `java -version` |
| Git | Any | ✅ Yes | `git --version` |
| pip packages | None | ❌ No | **Script uses standard library only!** |

### Installation by Platform

#### Ubuntu/Debian
```bash
sudo apt update && sudo apt install -y python3 python3-tk openjdk-17-jdk git curl
```

#### macOS
```bash
brew install python@3.11 openjdk@17 git python-tk
```

#### Windows
```powershell
winget install Python.Python.3.11
winget install EclipseAdoptium.Temurin.17.JDK
winget install Git.Git
```

#### Docker
```dockerfile
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 openjdk-17-jdk git curl
COPY scripts/ /app/scripts/
WORKDIR /app
ENTRYPOINT ["python3", "scripts/ig_publisher.py"]
```

## 📖 Usage Options

### 1. Command Line (Most Common)

```bash
# Auto-detect IG folder from publication-request.json
python ig_publisher.py

# Specify IG folder
python ig_publisher.py --ig-folder hiv

# Build without GitHub interaction (no token needed)
python ig_publisher.py --ig-folder hiv

# Build and create PRs (requires token)
python ig_publisher.py --push --github-token YOUR_TOKEN

# Debug mode with verbose output
python ig_publisher.py --ig-folder hiv --debug
```

### 2. GUI Interface

```bash
# Launch GUI
python ig_publisher.py --gui

# GUI with pre-filled settings
python ig_publisher_gui.py --ig-folder hiv --auto-build

# GUI in headless mode (no window)
python ig_publisher_gui.py --ig-folder hiv --no-gui
```

### 3. No-Token Version

```bash
# Build locally without any GitHub authentication
python ig_publisher_no_token.py --ig-folder hiv
```

## 📚 Command Line Reference

### Main Script Arguments

| Argument | Description | Default | Example |
|----------|-------------|---------|---------|
| `--ig-folder` | IG folder in webroot repo | Auto-detect from publication-request.json | `--ig-folder hiv` |
| `--webroot-repo` | Target repository for content | `WorldHealthOrganization/smart-html` | `--webroot-repo WHO/smart-html` |
| `--work-dir` | Working directory | Current directory | `--work-dir /path/to/work` |
| `--push` | Push changes and create PRs | False | `--push` |
| `--github-token` | GitHub token for PR creation | Environment: `GITHUB_TOKEN` | `--github-token ghp_xxx` |
| `--no-pr` | Push directly without PR | False | `--no-pr` |
| `--debug` | Enable debug logging | False | `--debug` |
| `--gui` | Launch GUI interface | False | `--gui` |

### GUI Script Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--auto-build` | Start build automatically | `--auto-build` |
| `--no-gui` | Run without GUI (headless) | `--no-gui` |
| `--theme` | GUI theme (light/dark) | `--theme dark` |
| `--config` | Load settings from JSON | `--config settings.json` |
| `--save-config` | Save settings to JSON | `--save-config my-config.json` |
| `--log-file` | Save output to file | `--log-file build.log` |

## ⚙️ Configuration

### publication-request.json

The script automatically reads this file to determine the IG folder:

```json
{
  "package-id": "who.fhir.smart.hiv",
  "version": "1.0.0",
  "path": "https://worldhealthorganization.github.io/smart-html/hiv",
  "status": "draft",
  "mode": "working"
}
```

### Environment Variables

```bash
export GITHUB_TOKEN=ghp_xxxxx       # GitHub token
export IG_FOLDER=hiv               # Default IG folder
export WEBROOT_REPO=WHO/smart-html # Default webroot repo
```

### Configuration File

Save settings in JSON:

```json
{
  "ig_folder": "hiv",
  "webroot_repo": "WorldHealthOrganization/smart-html",
  "push": true,
  "create_pr": true,
  "max_file_size": 100
}
```

Use with: `python ig_publisher.py --config my-settings.json`

## 📝 Examples

### Example 1: Simple Local Build

```bash
# Just build, no GitHub interaction
python ig_publisher.py --ig-folder hiv
```

Output structure:
```
./deploy/           # Ready to deploy files
./release-assets/   # Large files and package.tgz
./webroot/hiv/      # Sparse checkout of target folder
```

### Example 2: Full CI/CD Pipeline

```yaml
name: Complete IG Pipeline

on:
  push:
    branches: [main]

jobs:
  build-test-deploy:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
      - uses: actions/setup-java@v3
        with:
          java-version: '17'
      
      # Build IG
      - name: Build Implementation Guide
        id: build
        run: |
          python scripts/ig_publisher.py --debug
          echo "ig_folder=$(cat publication-request.json | python -c 'import json,sys;print(json.load(sys.stdin).get("path","").split("/")[-1])')" >> $GITHUB_OUTPUT
      
      # Run tests
      - name: Validate Output
        run: |
          test -f deploy/index.html
          test -f release-assets/package.tgz
      
      # Deploy
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./deploy
          destination_dir: ${{ steps.build.outputs.ig_folder }}
```

### Example 3: PR Creation Workflow

```yaml
name: Create PRs for IG Updates

on:
  workflow_dispatch:

jobs:
  create-prs:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
      - uses: actions/setup-java@v3
        with:
          java-version: '17'
      
      - name: Build and Create PRs
        env:
          # Requires PAT with repo access to external repos
          GITHUB_TOKEN: ${{ secrets.PAT_WITH_REPO_ACCESS }}
        run: |
          python scripts/ig_publisher.py \
            --push \
            --debug
      
      - name: Report PR URLs
        run: |
          echo "Check PR_INSTRUCTIONS.md for pull request links"
          cat PR_INSTRUCTIONS.md
```

### Example 4: Multi-Environment Deployment

```yaml
name: Deploy to Multiple Environments

on:
  push:
    branches: [main, staging, development]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
      - uses: actions/setup-java@v3
        with:
          java-version: '17'
      
      - name: Determine Environment
        id: env
        run: |
          if [[ "${{ github.ref }}" == "refs/heads/main" ]]; then
            echo "environment=production" >> $GITHUB_OUTPUT
            echo "url=https://worldhealthorganization.github.io/smart-html" >> $GITHUB_OUTPUT
          elif [[ "${{ github.ref }}" == "refs/heads/staging" ]]; then
            echo "environment=staging" >> $GITHUB_OUTPUT
            echo "url=https://staging.smart.who.int" >> $GITHUB_OUTPUT
          else
            echo "environment=development" >> $GITHUB_OUTPUT
            echo "url=https://dev.smart.who.int" >> $GITHUB_OUTPUT
          fi
      
      - name: Build IG
        run: python scripts/ig_publisher.py --debug
      
      - name: Deploy to ${{ steps.env.outputs.environment }}
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./deploy
          destination_dir: ${{ steps.env.outputs.environment }}
```

## 🐛 Troubleshooting

### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| `python: command not found` | Use `python3` instead of `python` |
| `java: command not found` | Install Java 17+: `apt install openjdk-17-jdk` |
| `No module named tkinter` | Install: `apt install python3-tk` (GUI only) |
| `Permission denied` | Run: `chmod +x ig_publisher.py` |
| `IG folder not specified` | Add `--ig-folder` or check `publication-request.json` |
| `GitHub API rate limit` | Use `--github-token` with PAT |
| `Disk space error` | Script already uses sparse checkout, check available space |

### Debug Mode

For detailed output:
```bash
python ig_publisher.py --ig-folder hiv --debug
```

### Check Requirements

```bash
python3 --version  # Should be 3.8+
java -version      # Should be 17+
git --version      # Any version
```

## 📁 Project Structure

```
your-ig-repo/
├── .github/
│   └── workflows/
│       └── build.yml           # GitHub Actions workflow
├── scripts/
│   ├── ig_publisher.py         # Main script
│   ├── ig_publisher_gui.py     # GUI module (optional)
│   └── ig_publisher_no_token.py # No-auth version
├── input/
│   └── fsh/                    # FHIR Shorthand files
├── publication-request.json    # IG configuration
└── sushi-config.yaml           # SUSHI configuration
```

## 🚢 Deployment Options

### GitHub Pages
```yaml
- uses: peaceiris/actions-gh-pages@v3
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    publish_dir: ./deploy
```

### AWS S3
```yaml
- uses: jakejarvis/s3-sync-action@master
  with:
    args: --acl public-read --follow-symlinks --delete
  env:
    AWS_S3_BUCKET: ${{ secrets.AWS_S3_BUCKET }}
    AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
    AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    SOURCE_DIR: './deploy'
```

### Docker Registry
```yaml
- name: Build and Push Docker Image
  run: |
    docker build -t ${{ secrets.REGISTRY }}/ig:${{ github.sha }} .
    docker push ${{ secrets.REGISTRY }}/ig:${{ github.sha }}
```

## 🔒 Security

- **No Token Mode**: Build without authentication using `ig_publisher_no_token.py`
- **Automatic Token**: GitHub Actions provides `GITHUB_TOKEN` automatically
- **PAT Required**: Only for pushing to external repositories
- **Sparse Checkout**: Minimizes code exposure by cloning only needed folders

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `python -m pytest tests/`
5. Submit a pull request

## 📞 Support

- **Documentation**: [Full docs](https://github.com/your-org/ig-publisher/wiki)
- **Issues**: [GitHub Issues](https://github.com/your-org/ig-publisher/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-org/ig-publisher/discussions)
- **FHIR Community**: [chat.fhir.org](https://chat.fhir.org)

## 🏆 Credits

Built for the WHO SMART Guidelines project by the FHIR community.

---

**Remember**: No pip packages required! Just Python standard library. 🎉