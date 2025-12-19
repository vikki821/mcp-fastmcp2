# Running Multiple Clients Simultaneously

## TL;DR

**Yes! You can run multiple clients at the same time!**

- **SSE/HTTP**: Multiple clients can connect to ONE server
- **STDIO**: Each client gets its OWN server instance

## How It Works

### Network Transports (SSE/HTTP)

```
        ┌─────────────────┐
        │   MCP Server    │
        │   (Port 8000)   │
        └─────────────────┘
         ↑      ↑      ↑
         │      │      │
    ┌────┘      │      └────┐
    │           │           │
Client 1    Client 2    Client 3
 (SSE)       (SSE)       (HTTP)
```

**One server, many clients!**

### STDIO Transport

```
Client 1 ──→ Server Instance 1
Client 2 ──→ Server Instance 2
Client 3 ──→ Server Instance 3
```

**Each client spawns its own server process.**

## Quick Demo

### Step 1: Start Multi-Transport Server

```bash
python run_multi_server.py
```

This starts ONE server that supports:
- SSE at `http://127.0.0.1:8000/sse`
- HTTP at `http://127.0.0.1:8000/mcp`

### Step 2: Connect Multiple Clients

**Terminal 1:**
```bash
python run_client.py sse
```

**Terminal 2:**
```bash
python run_client.py sse
```

**Terminal 3:**
```bash
python run_client.py stdio  # This creates its own server
```

**All three clients work simultaneously!**

## Programmatic Example

```python
import asyncio
from src.client.unified_client import MCPClient

async def client_1():
    client = MCPClient(transport="sse")
    await client.run()

async def client_2():
    client = MCPClient(transport="sse")
    await client.run()

async def client_3():
    client = MCPClient(transport="stdio")
    await client.run()

# Run all three at once
await asyncio.gather(client_1(), client_2(), client_3())
```

## Transport Comparison

| Transport | Server Instances | Concurrent Clients | Port Usage |
|-----------|-----------------|-------------------|------------|
| **SSE** | 1 shared | ✅ Unlimited | 1 port (8000) |
| **HTTP** | 1 shared | ✅ Unlimited | 1 port (8000) |
| **STDIO** | 1 per client | ✅ Unlimited | None |

## Use Cases

### Multiple SSE Clients (Shared Server)

**Perfect for:**
- Web applications with many users
- Dashboard with multiple viewers
- Microservices architecture
- Load testing

**Example:**
```bash
# Terminal 1: Start server once
python run_multi_server.py

# Terminals 2-10: Connect multiple clients
python run_client.py sse  # Client 1
python run_client.py sse  # Client 2
python run_client.py sse  # Client 3
# ... etc
```

### Multiple STDIO Clients (Separate Servers)

**Perfect for:**
- Parallel processing
- Isolated environments
- Testing different configurations
- Independent workflows

**Example:**
```bash
# Each command spawns its own server
python run_client.py stdio  # Server 1 + Client 1
python run_client.py stdio  # Server 2 + Client 2
python run_client.py stdio  # Server 3 + Client 3
```

### Mixed Transports

**Perfect for:**
- Hybrid architectures
- Migration scenarios
- Testing compatibility

**Example:**
```bash
# Terminal 1: Shared server for network clients
python run_multi_server.py

# Terminal 2: SSE client
python run_client.py sse

# Terminal 3: Another SSE client
python run_client.py sse

# Terminal 4: STDIO client (own server)
python run_client.py stdio
```

## Limitations

### Port Conflicts

You **cannot** run multiple network servers on the same port:

❌ **This won't work:**
```bash
python run_sse_server.py   # Uses port 8000
python run_http_server.py  # Also tries port 8000 - CONFLICT!
```

✅ **Solution 1: Use multi-transport server**
```bash
python run_multi_server.py  # Supports both SSE and HTTP
```

✅ **Solution 2: Use different ports**
```python
# Edit run_sse_server.py
mcp.run(transport="sse", port=8000)

# Edit run_http_server.py
mcp.run(transport="streamable-http", port=8001)
```

### STDIO Limitations

- Each STDIO client spawns a new Python process
- More memory usage with many STDIO clients
- No shared state between STDIO instances

## Advanced: Running on Different Ports

### Multiple SSE Servers

```python
# server_8000.py
from src.server.base_server import create_server
mcp = create_server("Server on 8000")
mcp.run(transport="sse", port=8000)

# server_8001.py
from src.server.base_server import create_server
mcp = create_server("Server on 8001")
mcp.run(transport="sse", port=8001)
```

Then connect:
```bash
python run_client.py sse --url http://127.0.0.1:8000/sse
python run_client.py sse --url http://127.0.0.1:8001/sse
```

## Testing Multiple Clients

Run the included demo:

```bash
# Make sure server is running
python run_multi_server.py

# In another terminal
python examples/multiple_clients.py
```

This will:
1. Connect 3 SSE clients to the shared server
2. Connect 2 STDIO clients (each with own server)
3. Show all 5 clients working simultaneously

## Performance Considerations

### SSE/HTTP (Shared Server)
- **Memory**: ~50MB base + ~1-5MB per client
- **CPU**: Minimal per client
- **Scalability**: Hundreds of clients easily

### STDIO (Per-Client Server)
- **Memory**: ~50MB per client
- **CPU**: One Python process per client
- **Scalability**: Dozens of clients (limited by system resources)

## Best Practices

1. **Use SSE/HTTP for multiple clients**
   - More efficient
   - Shared resources
   - Better scalability

2. **Use STDIO for isolation**
   - When you need separate server instances
   - For testing different configurations
   - When clients shouldn't share state

3. **Monitor resources**
   - Watch memory with many STDIO clients
   - Use connection pooling for HTTP clients
   - Implement rate limiting for production

4. **Handle disconnections**
   - SSE has built-in reconnection
   - Implement retry logic in clients
   - Monitor server health

## Summary

✅ **Multiple clients? YES!**
- SSE/HTTP: Many clients → One server
- STDIO: Many clients → Many servers
- Mixed: Both at the same time!

✅ **Same port? YES!**
- Multi-transport server supports SSE + HTTP
- Both on port 8000

✅ **Concurrent execution? YES!**
- All transports support concurrent clients
- No blocking or queuing

🚀 **Start experimenting:**
```bash
python run_multi_server.py
python examples/multiple_clients.py
```
