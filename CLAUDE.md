# Claude-Aware Dotfiles System

**Tools are available as shell scripts via Bash tool**

## Available Tools

### transcribe_youtube
- **User says:** "transcribe [youtube-url]" or "get text from [video]"
- **Shell command:** `~/.dotfiles/bin/transcribe_youtube <url> [filename]`
- **Auto-installs:** yt-dlp via Homebrew if missing
- **Features:** Working directory temps, minimal permissions

### create_tool
- **User says:** "let's create an atomic tool for [task]"
- **Shell command:** `~/.dotfiles/bin/create_tool <name> <description>`
- **Creates:** Permission-minimized shell script template
- **Features:** Built-in design rules, automated reminders

### network_drive_manager
- **User says:** "open latest 10 files in rated" or "list network files" or "open network drive movies2"
- **Shell command:** `~/.dotfiles/bin/network_drive_manager <command> [args]`
- **Auto-mounts:** SMB shares from PC (192.168.1.236) if not mounted
- **Features:** Natural language parsing, VLC playlist integration, smart file opening

### research_youtube_topic
- **User says:** "research YouTube videos on [topic]" or "find YouTube content about [subject]" or "compile YouTube research on [topic]"
- **Shell command:** `~/.dotfiles/bin/research_youtube_topic <subject> [timeframe] [num_videos]`
- **Performance limits:** Max 5 videos per topic, 2-30 min duration filter, 5min transcription timeout
- **Features:** Web search discovery, quality scoring, batch transcription, Claude-optimized JSON output
- **Output format:** `youtube.research.<subject-slug>.<timestamp>.json`
- **Examples:** 
  - `research_youtube_topic "AI news"` (3 videos from last week)
  - `research_youtube_topic "React tutorials" "last month" 5`
  - `research_youtube_topic "climate change" "last year" 2`

## Atomic Tool Style Guidelines

**ALL TOOLS MUST FOLLOW THESE UX PATTERNS:**

1. **Intuitive Output Names:**
   - Auto-generate meaningful filenames from content
   - Include identifiers for uniqueness (e.g., video ID, hash)
   - Format: `descriptive.words.IDENTIFIER.ext`
   - Limit filename length (~50 chars max)
   - Use dots to separate words for readability

2. **Smart Defaults:**
   - Minimize required parameters
   - Make optional parameters truly optional
   - Auto-detect and derive missing information when possible
   - Fail gracefully with clear error messages

3. **Consistent Patterns:**
   - Use same naming convention across all tools
   - Similar parameter patterns (url first, output optional)
   - Consistent return formats and messages
   - Standard success/error reporting

**Examples:**
- Video: `software.engineering.with.llms.2025.EO3_qN_Ynsk.txt`
- Audio: `podcast.episode.142.creativity.tools.AB7_xN_2kSw.mp3`
- Data: `stock.prices.apple.quarterly.20241215.csv`

## Atomic Tool Testing Protocol

**MANDATORY TESTING SEQUENCE:**

1. **Shell Script First:** Always create and test shell version before MCP
   - Create working shell script in `~/.dotfiles/bin/`
   - Test shell script manually with real inputs
   - Verify output is correct and complete
   - Only proceed to MCP after shell version works

2. **MCP Implementation:** Convert proven shell script to MCP
   - Use shell script logic as MCP function implementation
   - Replace placeholder code with actual working implementation
   - Test MCP function with same inputs used for shell testing

3. **Both Must Pass:** 
   - Shell script test: PASS ✅
   - MCP function test: PASS ✅
   - Only then commit and document new tool

4. **Testing Tools:**
   - Use `~/.dotfiles/bin/test_tool <tool_name> [args]` to test shell scripts
   - Test MCP functions via Claude after restart
   - Both versions must produce identical results

5. **Backup Strategy:**
   - Keep working shell script in backup/ directory  
   - If MCP fails, shell version provides reliable fallback

## Claude Code CLI Compatibility
- **Shell-first design:** All tools work as standalone shell scripts
- **No MCP dependency:** System works in both Claude Desktop and Claude Code CLI
- **Universal access:** Tools available via Bash tool in any Claude environment

## Creating New Atomic Tools
- **User trigger:** "let's create an atomic tool for this"
- **Process:**
  1. Run `~/.dotfiles/bin/create_tool <name> <description>` for shell template
  2. Follow permission-minimizing design rules (see Tool Development Standards)
  3. Test shell script until no permission prompts occur
  4. Update this CLAUDE.md with intent mapping
  5. Commit to git with clear description

**Automated Tool Creation:**
- Shell template: `~/.dotfiles/bin/create_tool <name> <description>`
- Includes permission-minimizing template with design rules
- Auto-generates proper file structure and placeholder code
- Works with Claude Code CLI (no MCP dependency)

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

### Core Principles
- Each tool is atomic (one function only)
- Auto-install dependencies when missing
- Use `which <tool>` checks before installing
- Log changes to git history (no separate changelog needed)

### Permission-Minimizing Design Rules

**CRITICAL: Tools must minimize permission requirements to avoid Claude CLI prompts**

1. **File Operations:**
   - Use working directory for temporary files: `TMP_DIR="./tmp_${tool_name}_$$"`
   - Avoid system `/tmp/` directory (requires `mktemp` permission)
   - Use `mkdir -p` instead of `mktemp -d`
   - Clean up with `rm -rf $TMP_DIR` in trap

2. **Command Consolidation:**
   - Minimize number of separate commands
   - Use built-in tool features instead of shell pipeline chains
   - Prefer single tools that do multiple operations
   - Example: `yt-dlp --sub-format txt` instead of `grep | sed | sort | uniq`

3. **Directory Navigation:**
   - Avoid `cd` when possible
   - Use absolute paths or tool output flags
   - Example: `yt-dlp -o "$TMP_DIR/%(title)s.%(ext)s"` instead of `cd && yt-dlp`

4. **Text Processing:**
   - Use `awk` instead of multiple `grep | sed | sort | uniq` chains
   - Single `awk` command can replace 5-10 separate commands
   - Reduces permission surface area significantly

5. **Permission Scope Strategy:**
   - List ALL required commands upfront in tool comments
   - Group related permissions together
   - Consider scoping global permissions to MCP tools only
   - Example header: `# REQUIRES: yt-dlp, mkdir, rm, awk, ls`

6. **Testing for Permissions:**
   - Test tools in fresh environments to catch permission issues
   - Document exact command list needed for global permissions
   - Prefer tools that work with minimal system access