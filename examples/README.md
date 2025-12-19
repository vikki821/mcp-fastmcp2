# Examples

## Using the Unified Client

The unified client allows you to switch between STDIO and SSE transports easily.

### Programmatic Usage

```python
from src.client.unified_client import MCPClient
import asyncio

async def main():
    # Use STDIO transport
    client = MCPClient(transport="stdio")
    await client.run()
    
    # Or use SSE transport
    client = MCPClient(transport="sse")
    await client.run(url="http://127.0.0.1:8000/sse")

asyncio.run(main())
```

### Command Line Usage

```bash
# STDIO transport (auto-starts server)
python run_client.py stdio

# SSE transport (requires server running)
python run_sse_server.py  # In terminal 1
python run_client.py sse   # In terminal 2
```

### Run the Example

```bash
# STDIO example (works immediately)
python examples/use_unified_client.py

# For SSE example, start server first:
python run_sse_server.py
```

## Benefits of Unified Client

1. **Single codebase** - One client handles both transports
2. **Easy switching** - Change transport with one parameter
3. **Consistent API** - Same methods work for both transports
4. **Less maintenance** - Update logic in one place
