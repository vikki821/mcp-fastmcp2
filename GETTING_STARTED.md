# Getting Started with MCP Project

## What is This?

This project demonstrates a complete implementation of the Model Context Protocol (MCP) using FastMCP2. It includes:
- ✅ A unified client that works with multiple transports
- ✅ STDIO transport (process-based)
- ✅ SSE transport (HTTP-based)
- ✅ Example tools and resources
- ✅ Clean, modular architecture

## 5-Minute Quick Start

### Step 1: Setup Environment

```bash
# Activate virtual environment (already created)
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Verify installation
python -c "import fastmcp; print('FastMCP installed!')"
```

### Step 2: Test STDIO (Easiest!)

```bash
python run_client.py stdio
```

**What happens:**
- Client automatically starts a server process
- Connects via standard input/output
- Calls tools and reads resources
- Shows results

**Expected output:**
```
✅ Connected to MCP server via STDIO

📦 Available tools:
  - add: Add two numbers together
  - multiply: Multiply two numbers
  - greet: Greet someone by name

🔢 add(10, 5) = 15
🔢 multiply(10, 5) = 50
👋 greet('FastMCP') = Hello, FastMCP!
...
```

### Step 3: Test SSE (HTTP-based)

**Terminal 1 - Start Server:**
```bash
python run_sse_server.py
```

**Terminal 2 - Run Client:**
```bash
python run_client.py sse
```

**What happens:**
- Server runs on http://127.0.0.1:8000/sse
- Client connects via HTTP
- Same tools and resources available
- Multiple clients can connect simultaneously

## Understanding the Code

### The Unified Client

The magic is in `src/client/unified_client.py`:

```python
from src.client.unified_client import MCPClient

# Create client with desired transport
client = MCPClient(transport="stdio")  # or "sse"

# Run it
await client.run()
```

### Adding Your Own Tools

Edit `src/server/base_server.py`:

```python
@mcp.tool()
def your_tool(param: str) -> str:
    """Your tool description"""
    return f"Result: {param}"
```

### Adding Your Own Resources

```python
@mcp.resource("myapp://data")
def get_data() -> str:
    """Get application data"""
    return "Your data here"
```

## Common Use Cases

### 1. Local Development (STDIO)
Perfect for:
- Testing tools quickly
- IDE integrations
- Local automation

```bash
python run_client.py stdio
```

### 2. Web Integration (SSE)
Perfect for:
- Web applications
- Remote access
- Multiple clients

```bash
# Start server once
python run_sse_server.py

# Connect from anywhere
python run_client.py sse
```

### 3. Programmatic Usage

```python
import asyncio
from src.client.unified_client import MCPClient

async def main():
    client = MCPClient(transport="stdio")
    await client.run()

asyncio.run(main())
```

## Project Structure Explained

```
mcp_project/
├── src/
│   ├── server/
│   │   └── base_server.py      # ⭐ Add your tools here
│   └── client/
│       └── unified_client.py   # ⭐ Unified client logic
├── run_client.py               # ⭐ Main entry point
├── run_sse_server.py           # Start SSE server
├── examples/                   # Usage examples
└── README.md                   # Full documentation
```

## Next Steps

1. **Explore Examples**
   ```bash
   python examples/use_unified_client.py
   ```

2. **Add Your Own Tools**
   - Edit `src/server/base_server.py`
   - Add `@mcp.tool()` decorated functions
   - Test with `python run_client.py stdio`

3. **Read Architecture**
   - See `ARCHITECTURE.md` for design details
   - Understand transport patterns
   - Learn about extensibility

4. **Deploy SSE Server**
   - Run `python run_sse_server.py`
   - Access from web apps
   - Scale horizontally

## Troubleshooting

### "Connection closed" error
- Make sure SSE server is running first
- Check if port 8000 is available
- Try STDIO instead: `python run_client.py stdio`

### Import errors
- Activate virtual environment
- Check `pip list | grep fastmcp`
- Reinstall: `pip install -r requirements.txt`

### Server won't start
- Check if port 8000 is in use
- Try different port in `run_sse_server.py`
- Use STDIO which doesn't need ports

## Resources

- **FastMCP Docs**: https://gofastmcp.com
- **MCP Spec**: https://modelcontextprotocol.io
- **This Project**: See README.md and ARCHITECTURE.md

## Support

Having issues? Check:
1. Virtual environment is activated
2. Dependencies are installed
3. Python version is 3.10+
4. For SSE: server is running first

Happy coding! 🚀
