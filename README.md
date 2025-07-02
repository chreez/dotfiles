# Dotfiles - Claude-Aware Tool System

Self-installing atomic tools that Claude can auto-discover across contexts.

## Quick Setup

```bash
curl -fsSL https://raw.githubusercontent.com/USER/dotfiles/main/install.sh | bash
```

## What This Does

- ✅ Claude reads `CLAUDE.md` and knows available tools instantly
- ✅ Tools auto-install missing dependencies 
- ✅ Atomic design - one tool, one job
- ✅ Lost laptop? One command restores everything

## Available Tools

- `transcribe_youtube` - Extract text from YouTube videos

## Adding New Tools

1. Add script to `bin/` directory
2. Make it executable: `chmod +x bin/toolname`
3. Update `CLAUDE.md` with one-line description
4. Git commit - no separate changelog needed

## Philosophy

Each tool is atomic and composable. Combine simple tools for complex workflows rather than building monolithic utilities.