#!/usr/bin/env python3
"""
A simple MCP server example in Python.

This server demonstrates how to create an MCP server with example tools
that can be called by MCP clients like Claude Code.
"""

import asyncio
import json
from mcp.server import Server
from mcp.types import Tool, TextContent
from mcp.server.stdio import stdio_server


# Create an MCP server instance
app = Server("example-server")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """
    List all available tools that this MCP server provides.

    Tools are functions that can be called by the MCP client.
    """
    return [
        Tool(
            name="add_numbers",
            description="Add two numbers together",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "First number"
                    },
                    "b": {
                        "type": "number",
                        "description": "Second number"
                    }
                },
                "required": ["a", "b"]
            }
        ),
        Tool(
            name="greet",
            description="Generate a personalized greeting",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Name of the person to greet"
                    }
                },
                "required": ["name"]
            }
        ),
        Tool(
            name="reverse_string",
            description="Reverse a string",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Text to reverse"
                    }
                },
                "required": ["text"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """
    Handle tool calls from the MCP client.

    This function is called when a client wants to execute one of the tools.
    """
    if name == "add_numbers":
        a = arguments["a"]
        b = arguments["b"]
        result = a + b
        return [TextContent(
            type="text",
            text=f"The sum of {a} and {b} is {result}"
        )]

    elif name == "greet":
        name_arg = arguments["name"]
        greeting = f"Hello, {name_arg}! Welcome to MCP!"
        return [TextContent(
            type="text",
            text=greeting
        )]

    elif name == "reverse_string":
        text = arguments["text"]
        reversed_text = text[::-1]
        return [TextContent(
            type="text",
            text=f"Reversed: {reversed_text}"
        )]

    else:
        raise ValueError(f"Unknown tool: {name}")


async def main():
    """Main entry point to run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
