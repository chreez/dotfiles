#!/usr/bin/env python3
"""
Chris's Dotfiles MCP Server
Atomic tools for Claude contexts
"""

import asyncio
import subprocess
import tempfile
import os
from pathlib import Path
from mcp.server import Server
from mcp.types import Tool, TextContent
import json
import re


app = Server("dotfiles-tools")


@app.tool()
async def transcribe_youtube(url: str, output_filename: str = "transcript.txt") -> list[TextContent]:
    """
    Extract text transcript from YouTube videos.
    
    Args:
        url: YouTube video URL to transcribe
        output_filename: Name for the output transcript file (default: transcript.txt)
    
    Returns:
        Success message with file location
    """
    
    # Create temporary directory and clean up on exit
    with tempfile.TemporaryDirectory() as tmp_dir:
        try:
            # Check if yt-dlp is installed, install if missing
            try:
                subprocess.run(["which", "yt-dlp"], check=True, capture_output=True)
            except subprocess.CalledProcessError:
                subprocess.run(["brew", "install", "yt-dlp"], check=True)
            
            # Extract subtitles to temporary directory
            subprocess.run([
                "yt-dlp", 
                "--write-subs", 
                "--write-auto-subs", 
                "--sub-langs", "en", 
                "--skip-download",
                url
            ], cwd=tmp_dir, check=True)
            
            # Find the VTT file
            vtt_files = list(Path(tmp_dir).glob("*.en.vtt"))
            if not vtt_files:
                return [TextContent(
                    type="text",
                    text="No subtitle file found. Video may not have subtitles available."
                )]
            
            vtt_file = vtt_files[0]
            
            # Clean up the VTT file to plain text
            with open(vtt_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Process content (remove VTT formatting)
            lines = content.split('\n')
            cleaned_lines = []
            
            for line in lines:
                line = line.strip()
                # Skip VTT headers, timestamps, and empty lines
                if (line and 
                    not line.startswith('WEBVTT') and
                    not line.startswith('Kind:') and
                    not line.startswith('Language:') and
                    not line.match(r'^\d+:\d+:\d+') and
                    not line.match(r'^\d+$')):
                    # Remove HTML tags
                    import re
                    line = re.sub(r'<[^>]*>', '', line)
                    if line.strip():
                        cleaned_lines.append(line.strip())
            
            # Remove duplicates while preserving order
            seen = set()
            final_lines = []
            for line in cleaned_lines:
                if line not in seen:
                    seen.add(line)
                    final_lines.append(line)
            
            # Write to output file
            output_path = Path.cwd() / output_filename
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(final_lines))
            
            return [TextContent(
                type="text",
                text=f"✅ Transcript saved to: {output_path}\n\nTranscript contains {len(final_lines)} lines of text."
            )]
            
        except subprocess.CalledProcessError as e:
            return [TextContent(
                type="text", 
                text=f"❌ Error during transcription: {e}"
            )]
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"❌ Unexpected error: {e}"
            )]


@app.tool()
async def create_atomic_tool(
    name: str, 
    description: str, 
    parameters: str,
    implementation_notes: str
) -> list[TextContent]:
    """
    Create a new atomic tool and add it to the MCP server.
    
    Args:
        name: Function name for the new tool (snake_case)
        description: What the tool does
        parameters: Parameter specifications (e.g., "url: str, output_file: str = 'output.txt'")
        implementation_notes: High-level implementation approach
        
    Returns:
        Success message with restart instructions
    """
    
    try:
        # Validate function name
        if not re.match(r'^[a-z][a-z0-9_]*$', name):
            return [TextContent(
                type="text",
                text="❌ Function name must be snake_case (lowercase letters, numbers, underscores)"
            )]
        
        # Generate the new tool function
        function_code = f'''

@app.tool()
async def {name}({parameters}) -> list[TextContent]:
    """
    {description}
    
    Implementation: {implementation_notes}
    """
    
    try:
        # TODO: Implement the actual functionality
        # This is a placeholder - replace with real implementation
        
        return [TextContent(
            type="text",
            text=f"✅ {name} executed successfully (placeholder implementation)"
        )]
        
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"❌ Error in {name}: {{e}}"
        )]
'''

        # Read current server file
        server_path = Path(__file__)
        with open(server_path, 'r') as f:
            content = f.read()
        
        # Check if function already exists
        if f"def {name}(" in content:
            return [TextContent(
                type="text",
                text=f"❌ Tool '{name}' already exists in server"
            )]
        
        # Insert new function before the main() function
        main_pos = content.find("async def main():")
        if main_pos == -1:
            return [TextContent(
                type="text",
                text="❌ Could not find main() function in server file"
            )]
        
        # Insert the new function
        new_content = content[:main_pos] + function_code + "\n\n" + content[main_pos:]
        
        # Write back to server file
        with open(server_path, 'w') as f:
            f.write(new_content)
        
        # Create restart script
        restart_script = f"""#!/bin/bash
# Auto-generated restart script for MCP server

echo "🔄 Restarting MCP server to load new tool: {name}"

# Kill existing server processes
pkill -f "dotfiles-tools" || true

# Wait a moment
sleep 2

echo "✅ Server restart complete"
echo "🔧 Restart Claude Desktop app to use new tool: {name}()"
echo "📝 Tool description: {description}"
"""
        
        restart_path = Path(__file__).parent / "restart.sh"
        with open(restart_path, 'w') as f:
            f.write(restart_script)
        
        os.chmod(restart_path, 0o755)
        
        return [TextContent(
            type="text",
            text=f"""✅ Created new atomic tool: {name}()

📝 Description: {description}
⚙️  Parameters: {parameters}
🔧 Implementation notes: {implementation_notes}

🚀 To activate:
1. Restart Claude Desktop app
2. Tool will be available as: {name}()

⚠️  Note: This is a placeholder implementation. Edit the function in:
   {server_path}
   
🔄 Restart script created at: {restart_path}"""
        )]
        
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"❌ Error creating tool: {e}"
        )]


async def main():
    # Import here to avoid issues if mcp is not installed
    from mcp.server.stdio import stdio_server
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())