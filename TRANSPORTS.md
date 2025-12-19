# MCP Transport Methods

## Overview

The Model Context Protocol (MCP) supports multiple transport methods for client-server communication. This project implements all transports supported by FastMCP2.

## Supported Transports

### 1. STDIO (Standard Input/Output) ✅

**What it is:**
- Process-based communication using standard input/output streams
- Server runs as a subprocess of the client
- Communication happens through stdin/stdout

**When to use:**
- Local development and testing
- IDE integrations (Claude Desktop, Cline, Cursor)
- Command-line tools
- Single-client scenarios
- When you need automatic server lifecycle management

**Advantages:**
- ✅ No network configuration needed
- ✅ Automatic server startup/shutdown
- ✅ Secure (local only)
- ✅ No port conflicts
- ✅ Simple setup

**Disadvantages:**
- ❌ Local only (no remote access)
- ❌ One client per server instance
- ❌ Process overhead for each client

**Example:**
```bash
python run_client.py stdio
```

**Server URL:** N/A (process-based)

---

### 2. SSE (Server-Sent Events) ✅

**What it is:**
- HTTP-based transport using Server-Sent Events
- Server runs independently on HTTP
- Client connects via HTTP and receives events via SSE

**When to use:**
- Web applications
- Remote access scenarios
- Multiple simultaneous clients
- When you need persistent connections
- Browser-based integrations

**Advantages:**
- ✅ Network accessible
- ✅ Multiple clients can connect
- ✅ Browser compatible
- ✅ Firewall friendly (uses HTTP)
- ✅ Built-in reconnection support

**Disadvantages:**
- ❌ Requires server to be running separately
- ❌ Port management needed
- ❌ One-way communication (server → client for events)

**Example:**
```bash
# Terminal 1: Start server
python run_sse_server.py

# Terminal 2: Connect client
python run_client.py sse
```

**Server URL:** `http://127.0.0.1:8000/sse`

---

### 3. HTTP (Streamable-HTTP) ✅

**What it is:**
- HTTP-based transport with streaming support
- Similar to SSE but uses different HTTP streaming mechanism
- Server runs independently on HTTP

**When to use:**
- When SSE is not suitable
- RESTful API integrations
- When you need standard HTTP semantics
- Proxy-friendly environments

**Advantages:**
- ✅ Standard HTTP protocol
- ✅ Works with HTTP proxies
- ✅ Multiple clients supported
- ✅ Network accessible

**Disadvantages:**
- ❌ Requires server to be running separately
- ❌ Port management needed
- ❌ More complex than STDIO

**Example:**
```bash
# Terminal 1: Start server
python run_http_server.py

# Terminal 2: Connect client
python run_client.py http
```

**Server URL:** `http://127.0.0.1:8000/mcp`

---

## Transport Comparison Table

| Feature | STDIO | SSE | HTTP |
|---------|-------|-----|------|
| **Network Access** | ❌ Local only | ✅ Yes | ✅ Yes |
| **Multiple Clients** | ❌ No | ✅ Yes | ✅ Yes |
| **Auto Server Start** | ✅ Yes | ❌ No | ❌ No |
| **Browser Support** | ❌ No | ✅ Yes | ✅ Yes |
| **Setup Complexity** | 🟢 Easy | 🟡 Medium | 🟡 Medium |
| **Port Required** | ❌ No | ✅ Yes | ✅ Yes |
| **Bidirectional** | ✅ Yes | ⚠️ Partial | ✅ Yes |
| **Reconnection** | N/A | ✅ Built-in | ⚠️ Manual |

## Other MCP Transports (Not in FastMCP)

### WebSocket ❌ Not Implemented

**What it is:**
- Full-duplex bidirectional communication
- Persistent connection over HTTP upgrade

**Status:** Not currently supported by FastMCP2

**When it might be useful:**
- Real-time bidirectional communication
- Low-latency requirements
- Gaming or chat applications

---

## Choosing the Right Transport

### Use STDIO when:
- 🎯 You're developing locally
- 🎯 You need the simplest setup
- 🎯 You're integrating with IDEs
- 🎯 You only need one client

### Use SSE when:
- 🎯 You need web browser support
- 🎯 You want multiple clients
- 🎯 You need server-to-client push
- 🎯 You're building a web app

### Use HTTP when:
- 🎯 You need standard HTTP semantics
- 🎯 You're working with HTTP proxies
- 🎯 SSE is blocked in your environment
- 🎯 You want RESTful patterns

---

## Implementation in This Project

### Unified Client
All three transports are supported through a single unified client:

```python
from src.client.unified_client import MCPClient

# STDIO
client = MCPClient(transport="stdio")
await client.run()

# SSE
client = MCPClient(transport="sse")
await client.run(url="http://127.0.0.1:8000/sse")

# HTTP
client = MCPClient(transport="http")
await client.run(url="http://127.0.0.1:8000/mcp")
```

### Command Line
```bash
python run_client.py stdio  # STDIO transport
python run_client.py sse    # SSE transport
python run_client.py http   # HTTP transport
```

---

## Technical Details

### STDIO Communication Flow
```
Client Process
    ↓ spawn
Server Process
    ↓ stdin/stdout
Communication
```

### SSE Communication Flow
```
Client → HTTP GET → Server
Server → SSE Stream → Client
Client → HTTP POST → Server (for requests)
```

### HTTP Communication Flow
```
Client → HTTP POST → Server
Server → HTTP Response (streaming) → Client
```

---

## Port Configuration

### Default Ports
- **SSE Server:** 8000 (endpoint: `/sse`)
- **HTTP Server:** 8000 (endpoint: `/mcp`)

### Changing Ports
Edit the server files:
```python
# run_sse_server.py or run_http_server.py
mcp.run(transport="sse", host="127.0.0.1", port=9000)
```

---

## Security Considerations

### STDIO
- ✅ Most secure (local only)
- ✅ No network exposure
- ✅ Process isolation

### SSE/HTTP
- ⚠️ Network exposed
- ⚠️ Consider adding authentication
- ⚠️ Use HTTPS in production
- ⚠️ Implement rate limiting
- ⚠️ Add CORS configuration

---

## Future Enhancements

Potential additions:
- WebSocket transport (when FastMCP adds support)
- TLS/SSL for HTTP transports
- Authentication middleware
- Connection pooling
- Load balancing for HTTP transports
