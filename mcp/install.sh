#!/bin/bash

# MCP Server Installation Script
# Sets up Python environment and installs MCP server

set -e

DOTFILES_DIR="$HOME/.dotfiles"
MCP_DIR="$DOTFILES_DIR/mcp"

echo "🐍 Setting up MCP server environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "$MCP_DIR/venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv "$MCP_DIR/venv"
fi

# Activate virtual environment and install dependencies
echo "Installing MCP dependencies..."
source "$MCP_DIR/venv/bin/activate"
pip install -r "$MCP_DIR/requirements.txt"

# Create MCP configuration for Claude
CLAUDE_CONFIG_DIR="$HOME/.claude"
mkdir -p "$CLAUDE_CONFIG_DIR"

# Add MCP server to Claude configuration
CLAUDE_CONFIG_FILE="$CLAUDE_CONFIG_DIR/claude_desktop_config.json"

if [ ! -f "$CLAUDE_CONFIG_FILE" ]; then
    echo '{}' > "$CLAUDE_CONFIG_FILE"
fi

# Update Claude config to include our MCP server
python3 << EOF
import json
import os

config_file = "$CLAUDE_CONFIG_FILE"
mcp_server_path = "$MCP_DIR/venv/bin/python3"
server_script = "$MCP_DIR/server.py"

# Read existing config
try:
    with open(config_file, 'r') as f:
        config = json.load(f)
except:
    config = {}

# Add MCP servers section if it doesn't exist
if 'mcpServers' not in config:
    config['mcpServers'] = {}

# Add our dotfiles tools server
config['mcpServers']['dotfiles-tools'] = {
    "command": mcp_server_path,
    "args": [server_script]
}

# Write updated config
with open(config_file, 'w') as f:
    json.dump(config, f, indent=2)

print(f"✅ Added dotfiles-tools MCP server to {config_file}")
EOF

echo "🔧 MCP server installed successfully!"
echo "📝 Restart Claude Desktop app to load new tools"
echo "🔍 Available tools: transcribe_youtube"