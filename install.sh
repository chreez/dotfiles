#!/bin/bash

# Dotfiles Installation Script
# Run: curl -fsSL https://raw.githubusercontent.com/USER/dotfiles/main/install.sh | bash

set -e

DOTFILES_DIR="$HOME/.dotfiles"
REPO_URL="https://github.com/chreez/dotfiles.git"

# Clone or update dotfiles
if [ -d "$DOTFILES_DIR" ]; then
    echo "📥 Updating dotfiles..."
    cd "$DOTFILES_DIR"
    git pull
else
    echo "📦 Cloning dotfiles..."
    git clone "$REPO_URL" "$DOTFILES_DIR"
    cd "$DOTFILES_DIR"
fi

# Make all bin scripts executable
chmod +x bin/*

# Add bin to PATH if not already there
if ! echo "$PATH" | grep -q "$DOTFILES_DIR/bin"; then
    echo 'export PATH="$HOME/.dotfiles/bin:$PATH"' >> ~/.zshrc
    echo "🔧 Added dotfiles/bin to PATH"
fi

# Create CLAUDE.md if it doesn't exist (for fresh clones)
if [ ! -f "CLAUDE.md" ]; then
    echo "📝 Creating CLAUDE.md..."
    echo "# Available Tools" > CLAUDE.md
    echo "Tools in bin/:" >> CLAUDE.md
    ls -1 bin/ | sed 's/^/- /' >> CLAUDE.md
fi

# Create workspace CLAUDE.md for tool inheritance
WORKSPACE_DIR="$HOME/workspace"
if [ -d "$WORKSPACE_DIR" ]; then
    echo "🔗 Adding Claude tools to workspace directory..."
    cat > "$WORKSPACE_DIR/CLAUDE.md" << EOF
# Workspace Tools

**Import dotfiles system:**
@$HOME/.dotfiles/CLAUDE.md

## Workspace Context
All projects in this workspace inherit Claude-aware tools from dotfiles.
EOF
fi

echo "✅ Dotfiles installed! Restart terminal or run: source ~/.zshrc"
echo "📋 Available tools:"
ls -1 bin/