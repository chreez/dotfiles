#!/usr/bin/env python3
"""
Chris's Dotfiles MCP Server - Minimal Working Version
"""

import asyncio
import subprocess
import tempfile
import os
import json
import re
from pathlib import Path
from mcp import types
from mcp.server import Server


# Simple working MCP server
server = Server("dotfiles-tools")


@server.list_tools()
async def list_tools() -> list[types.Tool]:
    """List available tools"""
    return [
        types.Tool(
            name="transcribe_youtube", 
            description="Extract text transcript from YouTube videos",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "YouTube video URL"},
                    "output_filename": {"type": "string", "description": "Optional output filename"}
                },
                "required": ["url"]
            }
        ),
        types.Tool(
            name="create_atomic_tool",
            description="Create framework for new atomic tool",
            inputSchema={
                "type": "object", 
                "properties": {
                    "name": {"type": "string", "description": "Tool name"},
                    "description": {"type": "string", "description": "What it does"},
                    "parameters": {"type": "string", "description": "Parameters"},
                    "notes": {"type": "string", "description": "Implementation notes"}
                },
                "required": ["name", "description", "parameters", "notes"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    """Handle tool calls"""
    
    if name == "transcribe_youtube":
        url = arguments["url"] 
        output_filename = arguments.get("output_filename")
        
        # Use the working shell script as fallback
        try:
            cmd = ["/Users/chris/.dotfiles/bin/transcribe_youtube", url]
            if output_filename:
                cmd.append(output_filename)
                
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            return [types.TextContent(
                type="text",
                text=f"✅ Transcription completed!\n\nOutput:\n{result.stdout}"
            )]
            
        except subprocess.CalledProcessError as e:
            return [types.TextContent(
                type="text",
                text=f"❌ Transcription failed: {e.stderr}"
            )]
            
    elif name == "create_atomic_tool":
        name = arguments["name"]
        description = arguments["description"] 
        parameters = arguments["parameters"]
        notes = arguments["notes"]
        
        return [types.TextContent(
            type="text",
            text=f"""✅ Atomic tool framework: {name}

📝 Description: {description}
⚙️  Parameters: {parameters}  
🔧 Notes: {notes}

🧪 TESTING PROTOCOL:
1. Create shell script: ~/.dotfiles/bin/{name}
2. Test shell script until it works
3. Replace this MCP framework with real implementation
4. Test MCP version
5. Both must pass ✅

⚠️  This is just the framework - implement the real functionality."""
        )]
        
    else:
        return [types.TextContent(
            type="text", 
            text=f"❌ Unknown tool: {name}"
        )]


if __name__ == "__main__":
    import mcp.server.stdio
    mcp.server.stdio.run_server(server)