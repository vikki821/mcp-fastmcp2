# Quick Reference Card

## Installation

```bash
git clone https://github.com/yourusername/mcp-fastmcp2.git
cd mcp-fastmcp2
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Running Clients

```bash
# STDIO (easiest - auto-starts server)
python run_client.py stdio

# SSE (requires server running)
python run_multi_server.py  # Terminal 1
python run_client.py sse     # Terminal 2

# HTTP
python run_multi_server.py  # Terminal 1
python run_client.py http    # Terminal 2
```

## Running Servers

```bash
# Multi-transport (SSE + HTTP)
python run_multi_server.py

# SSE only
python run_sse_server.py

# HTTP only
python run_http_server.py

# STDIO (auto-started by client)
# No manual start needed
```

## Programmatic Usage

```python
from src.client.unified_client import MCPClient
import asyncio

async def main():
    # STDIO
    client = MCPClient(transport="stdio")
    await client.run()
    
    # SSE
    client = MCPClient(transport="sse")
    await client.run(url="http://127.0.0.1:8000/sse")
    
    # HTTP
    client = MCPClient(transport="http")
    await client.run(url="http://127.0.0.1:8000/mcp")

asyncio.run(main())
```

## Adding Tools

Edit `src/server/base_server.py`:

```python
@mcp.tool()
def your_tool(param: str) -> str:
    """Tool description"""
    return f"Result: {param}"
```

## Adding Resources

Edit `src/server/base_server.py`:

```python
@mcp.resource("myapp://data")
def get_data() -> str:
    """Resource description"""
    return "Your data"
```

## Transport Comparison

| Feature | STDIO | SSE | HTTP |
|---------|-------|-----|------|
| Network | ❌ | ✅ | ✅ |
| Multi-client | ❌ | ✅ | ✅ |
| Auto-start | ✅ | ❌ | ❌ |
| Port | None | 8000 | 8000 |

## Common Commands

```bash
# Run examples
python examples/use_unified_client.py
python examples/multiple_clients.py

# Check server status
curl http://127.0.0.1:8000/sse

# View logs
# (Server output in terminal)
```

## File Structure

```
src/
├── client/
│   └── unified_client.py  # Main client
└── server/
    └── base_server.py     # Add tools here

run_client.py              # Run this!
run_multi_server.py        # Or this!
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Port in use | Change port in server file |
| Connection refused | Start server first (SSE/HTTP) |
| Import error | Activate venv, install deps |
| STDIO fails | Check Python path in client |

## URLs

- **SSE**: `http://127.0.0.1:8000/sse`
- **HTTP**: `http://127.0.0.1:8000/mcp`
- **Docs**: See README.md

## Help

```bash
python run_client.py --help
```

## Documentation

- `README.md` - Main docs
- `GETTING_STARTED.md` - Quick start
- `TRANSPORTS.md` - Transport details
- `MULTIPLE_CLIENTS.md` - Multi-client guide
- `ARCHITECTURE.md` - Design docs

---

**Need more help?** Check the full documentation or open an issue!
