# Dotfiles - Claude-Aware Tool System

Self-installing atomic tools that Claude can auto-discover across contexts.

## Quick Setup

```bash
curl -fsSL https://raw.githubusercontent.com/chreez/dotfiles/main/install.sh | bash
```

## What This Does

- ✅ Claude reads `CLAUDE.md` and knows available tools instantly
- ✅ Tools auto-install missing dependencies 
- ✅ Atomic design - one tool, one job
- ✅ Lost laptop? One command restores everything

## Available Tools

- `transcribe_youtube` - Extract text from YouTube videos
- `create_tool` - Generate atomic tool templates with permission-minimizing design
- `network_drive_manager` - Auto-mount SMB shares and manage network files
- `research_youtube_topic` - Discover and transcribe YouTube videos on topics
- `extract_youtube_audio` - Download audio from YouTube videos as MP3
- `transcribe_audio` - Convert audio files to text (local-first, privacy-focused)
- `download_song` - Search and download songs by name and artist
- `spec_validator` - Validate specification files using LLMs (techman integration)
- `spec_editor` - Create, update, and fork specification files (techman integration)
- `techman` - Complete specification workflow with AI assistance (techman integration)

## Adding New Tools

1. Add script to `bin/` directory
2. Make it executable: `chmod +x bin/toolname`
3. Update `CLAUDE.md` with intent mapping and description
4. **Update this README.md** with new tool in Available Tools section
5. Git commit - no separate changelog needed

## Philosophy

Each tool is atomic and composable. Combine simple tools for complex workflows rather than building monolithic utilities.