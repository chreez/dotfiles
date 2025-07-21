# Claude-Aware Dotfiles System

**Tools are available as shell scripts via Bash tool**

## Available Tools

### transcribe_youtube
- **User says:** "transcribe [youtube-url]" or "get text from [video]"
- **Shell command:** `~/.dotfiles/bin/transcribe_youtube <url> [filename]`
- **Auto-installs:** yt-dlp via Homebrew if missing
- **Features:** Working directory temps, minimal permissions
- **Important:** URLs with special characters (like ?) should be quoted to prevent shell expansion errors
- **Examples:**
  - `~/.dotfiles/bin/transcribe_youtube "https://www.youtube.com/watch?v=dQw4w9WgXcQ"`
  - `~/.dotfiles/bin/transcribe_youtube "https://youtu.be/dQw4w9WgXcQ" custom_name.txt`

### create_tool
- **User says:** "let's create an atomic tool for [task]"
- **Shell command:** `~/.dotfiles/bin/create_tool <name> <description>`
- **Creates:** Permission-minimized shell script template
- **Features:** Built-in design rules, automated reminders

### initClaude
- **User says:** "initialize claude project" or "create new workspace" or "start new project [name]" or "new workspace for [description]"
- **Shell command:** `~/.dotfiles/bin/initClaude [input] [--no-launch] [--file filename]`
- **Creates:** Project directories in ~/workspace/ with consistent dot-notation naming
- **Features:** AI-powered name generation, git initialization, template files, auto-launch Claude Code
- **Three input modes:** Natural language (AI suggests name), dot-notation (keeps as-is), direct name (converts to dots)
- **Auto-installs:** None (requires git, curl for AI APIs, claude-code CLI)
- **Examples:**
  - `~/.dotfiles/bin/initClaude` (creates scratch-YYYYMMDD workspace)
  - `~/.dotfiles/bin/initClaude "tool for parsing markdown files"` (AI suggests: markdown.parser)
  - `~/.dotfiles/bin/initClaude ml.parser` (creates ml.parser directory)
  - `~/.dotfiles/bin/initClaude data-viz` (converts to data.viz)
  - `~/.dotfiles/bin/initClaude --no-launch test.project` (create without launching Claude)
  - `echo "RSS feed aggregator" | ~/.dotfiles/bin/initClaude` (piped input)
  - `~/.dotfiles/bin/initClaude --file project-idea.txt` (file input)

### ssh_windows_wsl
- **User says:** "connect to windows" or "ssh to wsl" or "access windows host" or "ssh windows" or "run command on windows"
- **Shell command:** `~/.dotfiles/bin/ssh_windows_wsl [--command "cmd"] [--ip IP_ADDRESS]`
- **Always connects as user 'chris'** - no username parameter needed
- **Auto-discovery:** Scans network subnet if primary IP (192.168.1.236) fails
- **Features:** Network scanning, Chrome Remote Desktop startup instructions, fallback guidance, IP override, remote command execution via --command flag
- **Handles:** IP changes, WSL not running, computer offline scenarios
- **Examples:**
  - `~/.dotfiles/bin/ssh_windows_wsl` (connects to chris@192.168.1.236)
  - `~/.dotfiles/bin/ssh_windows_wsl --ip 192.168.1.100` (connects to chris@192.168.1.100)
  - `~/.dotfiles/bin/ssh_windows_wsl --command "docker ps"` (run command on default host)
  - `~/.dotfiles/bin/ssh_windows_wsl --command "ls -la"` (run command on default host)
  - `~/.dotfiles/bin/ssh_windows_wsl --ip 192.168.1.100 --command "uptime"` (run command on specific host)
  - `~/.dotfiles/bin/ssh_windows_wsl -c "systemctl status docker"` (short flag form)
  - `~/.dotfiles/bin/ssh_windows_wsl -i 192.168.1.100 -c "pwd"` (short flags combined)

### sync_windows_wsl
- **User says:** "sync files to windows" or "copy to wsl" or "upload to E drive" or "download from windows" or "rsync to remote"
- **Shell command:** `~/.dotfiles/bin/sync_windows_wsl [--to|--from] <path> [remote_path] [username] [ip_address]`
- **Safety restrictions:** Only allows E: drive (/mnt/e/), home directories (/home/), and temp (/tmp/) on remote
- **Features:** Bidirectional sync, safety validation, SSH connection testing, automatic directory creation
- **Auto-installs:** None (requires rsync, ssh, standard utilities)
- **Examples:**
  - `~/.dotfiles/bin/sync_windows_wsl ./myfile.txt` (copy to E:/myfile.txt)
  - `~/.dotfiles/bin/sync_windows_wsl ./docs/ /mnt/e/backup/` (sync directory to E:/backup/)
  - `~/.dotfiles/bin/sync_windows_wsl --from /mnt/e/data.txt ./` (download from E: drive)
  - `~/.dotfiles/bin/sync_windows_wsl ./project/ /home/chris/work/` (sync to home directory)
  - `~/.dotfiles/bin/sync_windows_wsl ./file.txt /mnt/e/ admin 192.168.1.100` (custom user/IP)

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

### extract_youtube_audio
- **User says:** "extract audio from [youtube-url]" or "download music from [video]" or "get mp3 from [youtube]"
- **Shell command:** `~/.dotfiles/bin/extract_youtube_audio <url> [filename]`
- **Auto-installs:** yt-dlp via Homebrew if missing
- **Features:** Working directory temps, minimal permissions, smart filename generation
- **Important:** URLs with special characters (like ?) should be quoted to prevent shell expansion errors
- **Examples:**
  - `~/.dotfiles/bin/extract_youtube_audio "https://www.youtube.com/watch?v=dQw4w9WgXcQ"`
  - `~/.dotfiles/bin/extract_youtube_audio "https://youtu.be/dQw4w9WgXcQ" my_song.mp3`

### transcribe_audio
- **User says:** "transcribe [audio-file]" or "convert audio to text" or "speech to text [file]"
- **Shell command:** `~/.dotfiles/bin/transcribe_audio <audio_file> [output_file] [--cloud] [--model=small|medium|large-v3-turbo]`
- **Auto-installs:** whisper-cpp, ffmpeg via Homebrew if missing
- **Features:** Local-first privacy, smart model selection, cloud fallback, format conversion
- **Privacy:** Local processing by default, cloud only with --cloud flag or as fallback
- **Model selection:** Auto-selects based on file size (small<10MB, medium<50MB, large-v3-turbo>50MB)
- **Examples:**
  - `~/.dotfiles/bin/transcribe_audio podcast.mp3`
  - `~/.dotfiles/bin/transcribe_audio interview.wav transcript.txt`
  - `~/.dotfiles/bin/transcribe_audio long_file.mp3 --cloud`
  - `~/.dotfiles/bin/transcribe_audio speech.mp3 --model=large-v3-turbo`

### download_song
- **User says:** "download song [name]" or "get song [title] by [artist]" or "download music [song name]"
- **Shell command:** `~/.dotfiles/bin/download_song <song_name> [artist_name] [output_directory]`
- **Auto-installs:** yt-dlp via Homebrew if missing
- **Features:** YouTube search integration, smart naming, artist preference, directory selection
- **Output format:** `artist.song.title.mp3` or `song.title.mp3` (without artist)
- **Examples:**
  - `~/.dotfiles/bin/download_song "Bohemian Rhapsody" "Queen"`
  - `~/.dotfiles/bin/download_song "Yesterday" "The Beatles" ~/Music/`
  - `~/.dotfiles/bin/download_song "Imagine"` (searches without artist)

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

6. **Git Commit Requirement:**
   - **MANDATORY:** Every fully tested tool must be committed to git
   - Commit message format: `Add <tool_name>: <brief_description>`
   - Include test results and usage examples in commit message
   - Ensure .dotfiles directory is clean after commit (no untracked files)
   - Use `git status` to verify clean state before proceeding

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
  5. **MANDATORY:** Update README.md with new tool in Available Tools section
  6. **MANDATORY:** Commit to git with clear description after full testing
  7. **MANDATORY:** Ensure .dotfiles directory is clean after commit

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

## Memories and Best Practices

- **Tool Testing:** Make sure to clean up tmp files when testing tools before committing