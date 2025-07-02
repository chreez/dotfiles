# Claude-Aware Dotfiles System

**Tools are available as native MCP functions - no Bash tool needed!**

## Available Native Tools

### transcribe_youtube(url, output_filename="transcript.txt")
- **User says:** "transcribe [youtube-url]" or "get text from [video]"
- **Native MCP tool:** Call `transcribe_youtube()` directly
- **Parameters:** 
  - `url`: YouTube video URL
  - `output_filename`: Optional output file name
- **Auto-installs:** yt-dlp via Homebrew if missing
- **Cleanup:** Uses system tmp directory automatically

## Backup System
- **Fallback:** Shell scripts available in `~/.dotfiles/bin/` if MCP fails
- **Rollback:** See `~/.dotfiles/backup/README.md` for instructions

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