# Claude-Aware Dotfiles System

**Always check `~/.dotfiles/bin/` before solving problems - tools may already exist.**

## Intent → Tool Mapping

### YouTube/Video Transcription
- **User says:** "transcribe [youtube-url]" or "get text from [video]"
- **Tool:** `transcribe_youtube <url> [output.txt]` in ~/.dotfiles/bin/
- **Action:** Use existing tool via Bash: `/Users/chris/.dotfiles/bin/transcribe_youtube <url>`
- **Notes:** Handles large files piecemeal (use Read tool with offset/limit), auto-installs yt-dlp

## Creating New Atomic Tools
- **User trigger:** "let's create an atomic tool for this"
- **Process:**
  1. Extract core function from recent work
  2. Make it dependency-checking & auto-installing  
  3. Add to ~/.dotfiles/bin/ with descriptive name
  4. Update this CLAUDE.md with intent mapping
  5. Commit to git with clear description

## Tool Discovery Rules
- **FIRST STEP:** Always check ~/.dotfiles/bin/ for ANY part of the task
- Break complex requests into steps, check tools for EACH step
- Example: "Transcribe video + build website" = Step 1: transcribe (check tools), Step 2: build site
- Map user intent to existing tools when possible
- If no tool exists → solve normally, then offer to atomize
- Ask: "Should we create a tool for this recurring task?"

## Installation
- One-time setup: `curl -fsSL https://raw.githubusercontent.com/chreez/dotfiles/main/install.sh | bash`
- Manual: `git clone https://github.com/chreez/dotfiles.git ~/.dotfiles && ~/.dotfiles/install.sh`

## Tool Development Standards
- Each tool is atomic (one function only)
- Auto-install dependencies when missing
- Use `which <tool>` checks before installing
- Use system tmp directory: `TMP_DIR=$(mktemp -d)` + `trap "rm -rf $TMP_DIR" EXIT`
- Log changes to git history (no separate changelog needed)