# Backup & Rollback Instructions

## Current System Status
- **Primary:** MCP Server (native Claude tools)
- **Backup:** Shell scripts (via Bash tool)

## Rollback to Shell Scripts

If MCP isn't working, restore shell script functionality:

1. **Restore PATH access:**
   ```bash
   export PATH="$HOME/.dotfiles/bin:$PATH"
   ```

2. **Update CLAUDE.md to use shell tools:**
   ```markdown
   ### YouTube/Video Transcription  
   - **User says:** "transcribe [youtube-url]"
   - **Tool:** Use Bash tool: `/Users/chris/.dotfiles/bin/transcribe_youtube <url>`
   ```

3. **Copy backup script if needed:**
   ```bash
   cp ~/.dotfiles/backup/transcribe_youtube_shell.sh ~/.dotfiles/bin/transcribe_youtube
   chmod +x ~/.dotfiles/bin/transcribe_youtube
   ```

## Files Backed Up
- `transcribe_youtube_shell.sh` - Original working shell script
- This README with rollback instructions

## Testing Rollback
Test shell script manually:
```bash
~/.dotfiles/bin/transcribe_youtube "https://www.youtube.com/watch?v=VIDEO_ID"
```