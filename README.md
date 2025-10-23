# MCP Server Example (Python)

A simple Model Context Protocol (MCP) server implementation in Python.

## What is MCP?

The Model Context Protocol (MCP) is an open protocol that enables AI assistants like Claude to securely interact with external tools and data sources. MCP servers expose tools that clients can discover and call.

## Project Structure

```
mcp_playground/
├── server.py           # Main MCP server implementation
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Setup

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. Clone this repository (if you haven't already)

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

To run the MCP server:

```bash
python server.py
```

The server uses stdio (standard input/output) for communication, which is the standard way MCP servers communicate with clients.

## Available Tools

This example server provides three simple tools:

### 1. add_numbers
Adds two numbers together.

**Parameters:**
- `a` (number): First number
- `b` (number): Second number

**Example:**
```json
{
  "a": 5,
  "b": 3
}
```

### 2. greet
Generates a personalized greeting.

**Parameters:**
- `name` (string): Name of the person to greet

**Example:**
```json
{
  "name": "Alice"
}
```

### 3. reverse_string
Reverses a string.

**Parameters:**
- `text` (string): Text to reverse

**Example:**
```json
{
  "text": "Hello World"
}
```

## Using with Claude Code

To use this MCP server with Claude Code, you need to configure it in your MCP settings:

1. Open your Claude Code MCP configuration file (typically at `~/.config/claude/claude_desktop_config.json`)

2. Add this server to the `mcpServers` section:

```json
{
  "mcpServers": {
    "example-server": {
      "command": "python",
      "args": ["/path/to/mcp_playground/server.py"]
    }
  }
}
```

3. Restart Claude Code

4. The tools will now be available for Claude to use!

## Customizing the Server

### Adding New Tools

To add a new tool to the server:

1. Add the tool definition to the `list_tools()` function
2. Add the tool implementation to the `call_tool()` function

Example:

```python
# In list_tools():
Tool(
    name="my_new_tool",
    description="Description of what the tool does",
    inputSchema={
        "type": "object",
        "properties": {
            "param1": {
                "type": "string",
                "description": "Parameter description"
            }
        },
        "required": ["param1"]
    }
)

# In call_tool():
elif name == "my_new_tool":
    param1 = arguments["param1"]
    result = do_something(param1)
    return [TextContent(
        type="text",
        text=f"Result: {result}"
    )]
```

### Advanced Features

The MCP protocol supports additional features beyond basic tools:

- **Resources**: Expose data that can be read (files, API data, etc.)
- **Prompts**: Provide templated prompts
- **Sampling**: Allow the server to request LLM completions

Check the [MCP documentation](https://modelcontextprotocol.io) for more information.

## Development

### Running in Development Mode

For development, you might want to add logging:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

### Testing

You can test your MCP server using the MCP Inspector tool or by integrating it directly with Claude Code.

## Troubleshooting

### "Module not found" errors
Make sure you've installed the dependencies:
```bash
pip install -r requirements.txt
```

### Server not appearing in Claude Code
- Check that the path in your MCP configuration is correct
- Make sure the virtual environment is activated (if using one)
- Try restarting Claude Code

### Tool calls failing
- Check the server logs for error messages
- Verify that the input schema matches what you're passing
- Make sure all required parameters are provided

## Resources

- [MCP Documentation](https://modelcontextprotocol.io)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Specification](https://spec.modelcontextprotocol.io)

## License

This is an example project for educational purposes.
