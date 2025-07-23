---
id: initClaude
version: 0.1.0
title: Semantic Claude Workspace Initializer
status: draft
entry_points:
  - ~/.dotfiles/bin/initClaude
description: >
  Initializes a Claude-compatible project directory in ~/workspace/ with consistent, short naming,
  Git init, and file scaffolding, then launches Claude Code in the new directory for immediate development.
---

## 🧠 Goal

Automate the creation of short, consistent project folders using natural language or explicit inputs. Enable agent-ready environments with one command. Reduce setup friction and enforce workspace consistency.

## ✅ Success Criteria

* Accepts input in three modes:
  * **Natural language**: e.g. "create a tool for parsing markdown files" → AI suggests name
  * **Dot-notation**: e.g. `ml.parser` → keeps as-is
  * **Direct name**: e.g. `data-viz` → converts to `data.viz`
* No input creates dated scratch: `~/workspace/scratch-YYYYMMDD`
* Named projects create clean directories: `~/workspace/{project.name}`
* Project names always use dot notation: `word.word.word` (max 3 words)
* Adds 4-char UUID suffix only on collision: `{project.name}-xxxx`
* Directory includes:
  * `.git/` (initialized)
  * `CLAUDE.md` (empty template)
  * `README.md` (formatted with project info)
  * `.gitignore` (basic template)
* Initial commit: "Initialize project: {project.name}"
* **Automatically changes to new directory and launches Claude Code**
* Interactive launch can be disabled with `--no-launch` flag (for testing)
* If directory exists, changes to it and launches Claude Code
* Small, shell-based implementation
* API keys from environment variables (fallback between Claude/GPT on error)
* Accepts piped input: `echo "ML parser tool" | initClaude`
* Accepts file input: `initClaude --file idea.txt`
* NO LLM call for empty input (scratch mode)

## 🧪 Test Strategy

* Test natural language → API name generation
* Test dot-notation → passthrough behavior
* Test direct names → dot conversion behavior
* Test empty input → scratch-YYYYMMDD format (no API call)
* Test collision → UUID suffix addition
* Test existing directory → changes to it and launches Claude
* Test `--no-launch` flag prevents Claude Code launch
* Test piped and file inputs
* Test API fallback (Claude → GPT)
* Verify git initialization and commit
* Validate generated file contents
* Verify Claude Code launches in correct directory

## 📁 Directory Structure

### Named Projects
```
~/workspace/{project.name}/
├── .git/              # Initialized git repository
├── CLAUDE.md          # Empty Claude instructions template
├── README.md          # Project summary with metadata
└── .gitignore         # Basic ignore patterns
```

### Scratch Projects
```
~/workspace/scratch-YYYYMMDD/
├── .git/              # Initialized git repository
├── CLAUDE.md          # Empty Claude instructions template
├── README.md          # Project summary with metadata
└── .gitignore         # Basic ignore patterns
```

## 📄 File Templates

### README.md
```markdown
# {Project Title}

🧪 *Initialized {YYYY-MM-DD}* — `{directory.name}`

## Description
{Original input text or "Scratch workspace for quick experiments"}

## Getting Started
```bash
claude-code .
```

## Notes
- [ ] Fill out CLAUDE.md with project context
- [ ] Add specific implementation details
- [ ] Update description as needed
```

### CLAUDE.md
```markdown
# Project Context for Claude

## Project: {directory.name}
*Initialized: {YYYY-MM-DD}*

## Overview
{Empty - to be filled by user}

## Key Files
{Empty - to be filled by user}

## Current Tasks
{Empty - to be filled by user}
```

### .gitignore
```
.DS_Store
*.log
node_modules/
__pycache__/
.env
```

## 🔠 Naming Logic

### Output Format
All projects use dot-separated format: `word.word.word` (1-3 words max)

### Input Processing
1. **Natural language** (contains spaces or descriptive phrases):
   - Input: `"create a markdown parser tool"`
   - API call: "Generate a 1-3 word project name for: {input}"
   - API response: `markdown.parser`
   - Final: `~/workspace/markdown.parser/`

2. **Dot-notation** (already contains dots):
   - Input: `ml.parser`
   - Use as-is: `ml.parser`
   - Final: `~/workspace/ml.parser/`

3. **Direct name** (contains hyphens/underscores):
   - Input: `data-viz`
   - Convert: `data.viz`
   - Final: `~/workspace/data.viz/`

4. **Empty input** (no LLM call):
   - Default: `~/workspace/scratch-20250720/`

### Collision Handling
- First attempt: `~/workspace/project.name/`
- If exists: `~/workspace/project.name-a3f2/` (first 4 chars of UUID)

### LLM Fallback Naming
If LLM fails or returns unusable name:
- Convert input directly: spaces/hyphens → dots
- Truncate to 3 words max
- Example: "my awesome project idea" → `my.awesome.project`

## 🔧 Implementation Details

### Environment Setup
```bash
# In ~/.zshrc or ~/.bashrc
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."

# Aliases
alias newp="~/.dotfiles/bin/initClaude"
alias scratch="~/.dotfiles/bin/initClaude"  # Creates scratch-YYYYMMDD and launches Claude
```

### API Configuration
- Primary: Claude API (if ANTHROPIC_API_KEY exists)
- Fallback: OpenAI GPT (if OPENAI_API_KEY exists)
- API prompt: "Generate a short project name (1-3 words) for: {input}. Output ONLY the name in lowercase using dots between words. Examples: ml.parser, data.viz.tool, web.scraper. Maximum 3 words."
- Skip API entirely for empty input

### Usage Examples
```bash
# Natural language (creates and launches)
$ initClaude "tool for parsing markdown files"
→ Creates: ~/workspace/markdown.parser/
→ Launches: claude-code in new directory

# Dot-notation (already formatted)
$ initClaude ml.parser
→ Creates: ~/workspace/ml.parser/
→ Launches: claude-code in new directory

# Direct name (converts hyphens to dots)
$ initClaude data-viz
→ Creates: ~/workspace/data.viz/
→ Launches: claude-code in new directory

# No input (scratch with date, no API call)
$ initClaude
→ Creates: ~/workspace/scratch-20250720/
→ Launches: claude-code in new directory

# Testing mode (no launch)
$ initClaude --no-launch ml.parser
→ Creates: ~/workspace/ml.parser/
→ Exits without launching Claude

# Piped input
$ echo "RSS feed aggregator" | initClaude
→ Creates: ~/workspace/rss.aggregator/
→ Launches: claude-code in new directory

# File input
$ initClaude --file project-idea.txt
→ Creates: ~/workspace/feed.reader/
→ Launches: claude-code in new directory

# Collision handling
$ initClaude data.viz  # (if data.viz exists)
→ Creates: ~/workspace/data.viz-8a3f/
→ Launches: claude-code in new directory

# Existing directory (just launches)
$ initClaude ml.parser  # (if ml.parser exists)
→ Directory exists: ~/workspace/ml.parser/
→ Launches: claude-code in existing directory
```

### Output Messages
```bash
# Success (named project)
✨ Created project: ~/workspace/markdown.parser/
📝 Initialized with README.md, CLAUDE.md, and git
🚀 Launching Claude Code...

# Success (scratch)
✨ Created scratch workspace: ~/workspace/scratch-20250720/
📝 Ready for quick experiments
🚀 Launching Claude Code...

# Directory exists (still launches)
🌸 Project already exists: ~/workspace/data.viz/
🚀 Launching Claude Code...

# Testing mode
✨ Created project: ~/workspace/ml.parser/
📝 Initialized with README.md, CLAUDE.md, and git
✅ Test mode: Claude Code not launched

# API failure (falls back to direct conversion)
⚠️  Could not reach AI service, using direct conversion
✨ Created project: ~/workspace/tool.for.parsing/
🚀 Launching Claude Code...
```

## 🔁 Changelog

* 0.1.0 — 2025-07-20 — Initial specification with auto-launch Claude Code, renamed to initClaude