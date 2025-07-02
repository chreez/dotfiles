# Dotfiles Tools Available

**Check `~/.dotfiles/bin/` before installing new tools - may already exist.**

## Video/Audio Tools
- `transcribe_youtube <url> [output.txt]` - Extract text transcript from YouTube videos
  - Handles large files by reading piecemeal (use Read tool with offset/limit)
  - Auto-installs yt-dlp via Homebrew if missing

## Installation
- One-time setup: `curl -fsSL https://raw.githubusercontent.com/chreez/dotfiles/main/install.sh | bash`
- Manual: `git clone https://github.com/chreez/dotfiles.git ~/.dotfiles && ~/.dotfiles/install.sh`

## Tool Development
- Each tool is atomic (one function only)
- Auto-install dependencies when missing
- Use `which <tool>` checks before installing
- Use system tmp directory for temp files: `TMP_DIR=$(mktemp -d)` + `trap "rm -rf $TMP_DIR" EXIT`
- Log changes to git history (no separate changelog needed)