# GitHub Repository Setup Guide

This guide covers the improvements made to your RPS World repository and the manual steps needed on GitHub.

## ✅ Files Created

### 1. `.gitattributes`
Tells GitHub's Linguist to treat documentation as non-code, ensuring the repo is classified as Python.

### 2. `pyproject.toml`
Modern Python packaging configuration file that:
- Declares project metadata (name, version, description)
- Lists dependencies
- Defines the `rps-world` command-line script
- Makes the project pip-installable

### 3. Updated `README.md`
Enhanced with:
- Badges (Python version, license, platform, CI status)
- Quick start guide with virtual environment setup
- GitHub Pages link
- Better formatting and emojis

### 4. `docs/index.md`
GitHub Pages landing page with:
- Project overview and features
- Installation instructions
- Game rules and controls
- Links to documentation
- Professional layout

### 5. `.github/workflows/python.yml`
GitHub Actions CI workflow that:
- Runs on push and pull requests
- Tests on Python 3.10, 3.11, and 3.12
- Runs your test suite automatically
- Verifies the module can be imported
- Uses dummy SDL drivers for headless testing

## 🚀 Next Steps on GitHub

### Step 1: Commit and Push Changes

```bash
git add .
git commit -m "Add Python packaging, CI/CD, and GitHub Pages setup"
git push origin master
```

### Step 2: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. Scroll down to **Pages** (left sidebar)
4. Under **Source**, select:
   - Branch: `master` (or `main`)
   - Folder: `/docs`
5. Click **Save**
6. Wait 1-2 minutes, then visit: `https://cretzuwashere.github.io/RPS/`

### Step 3: Add Repository Topics

1. On your repo's main page, click the **⚙️ gear icon** next to "About" (right side)
2. Add these topics:
   - `python`
   - `pygame`
   - `game`
   - `simulation`
   - `rock-paper-scissors`
   - `agent-based-simulation`
3. Click **Save changes**

### Step 4: Add a Social Preview Image (Optional but Recommended)

1. Run your game and take a nice screenshot during gameplay
2. Go to **Settings** → **Options** (left sidebar)
3. Scroll to **Social preview**
4. Click **Upload an image**
5. Upload a screenshot (recommended size: 1200x630 px)

This image will appear when someone shares your repo on social media!

### Step 5: Update Repository Description

1. On your repo's main page, click the **⚙️ gear icon** next to "About"
2. Add description: "Rock–Paper–Scissors world simulation with named agents, hunting behavior, and victory detection - built with Python & Pygame"
3. Add website: `https://cretzuwashere.github.io/RPS/`
4. Check ☑️ "Releases" if you plan to create releases later
5. Click **Save changes**

## 🎯 Testing the Package Installation

After pushing, test the new package configuration:

```bash
# Install in editable mode
pip install -e .

# Run using the new command
rps-world

# Or the traditional way still works
python -m rps.app
```

## 📊 Monitor CI Status

After your first push, you can:
- See the CI workflow running under the **Actions** tab
- The badge in README.md will show build status (passing/failing)
- Each push/PR will automatically run tests

## 🎨 Add a Screenshot (Highly Recommended)

1. Run the game: `python -m rps.app`
2. Press `B` to spawn agents
3. Take a screenshot during gameplay
4. Save as `docs/screenshot.png`
5. Commit and push:
   ```bash
   git add docs/screenshot.png
   git commit -m "Add gameplay screenshot"
   git push
   ```

The screenshot will automatically appear on your GitHub Pages site!

## 🔍 Verify Everything Works

After completing the steps:

1. ✅ GitHub recognizes repo as Python (language bar shows Python as dominant)
2. ✅ CI badge shows green (passing tests)
3. ✅ Topics appear below the repo description
4. ✅ GitHub Pages site is live
5. ✅ Social preview image appears when sharing
6. ✅ Package can be installed with `pip install -e .`

## 📝 What Each File Does

| File | Purpose |
|------|---------|
| `.gitattributes` | Controls GitHub language detection |
| `pyproject.toml` | Modern Python package metadata |
| `.github/workflows/python.yml` | Automated testing on GitHub |
| `docs/index.md` | GitHub Pages landing page |
| `docs/README.md` | Instructions for adding screenshots |

## 🎉 Benefits

Your repository now has:
- ✅ Professional README with badges
- ✅ Proper Python packaging (pip installable)
- ✅ Automated CI/CD testing
- ✅ Beautiful GitHub Pages site
- ✅ Clear language detection (Python)
- ✅ Easy discovery via topics
- ✅ Social media preview support

## 🐛 Troubleshooting

### CI Workflow Fails
- Check Python version compatibility
- Ensure all dependencies are in `requirements.txt`
- Review error logs in Actions tab

### GitHub Pages Not Working
- Ensure `docs/index.md` exists
- Check Pages settings point to `/docs` folder
- Wait 2-3 minutes after enabling

### Language Detection Wrong
- Push the `.gitattributes` file
- Wait for GitHub to re-analyze (can take a few hours)
- Most code should be `.py` files (already true for your repo)

## 📚 References

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python Packaging Guide](https://packaging.python.org/)
- [Shields.io Badges](https://shields.io/)

