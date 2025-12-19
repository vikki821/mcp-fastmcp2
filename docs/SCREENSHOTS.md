# Screenshots and Examples

## Server Starting

### Multi-Transport Server
```
╭──────────────────────────────────────────────────────────────────────────────╮
│                                                                              │
│ ▄▀▀ ▄▀█ █▀▀ ▀█▀ █▀▄▀█ █▀▀ █▀█                                              │
│ █▀  █▀█ ▄▄█  █  █ ▀ █ █▄▄ █▀▀                                              │
│                                                                              │
│ FastMCP 2.14.1                                                               │
│                                                                              │
│                                                                              │
│ 🖥  Server name: MCP Multi-Transport Server                                 │
│                                                                              │
│ 📦 Transport:   SSE                                                          │
│ 🔗 Server URL:  http://127.0.0.1:8000/sse                                   │
│                                                                              │
│ 📚 Docs:        https://gofastmcp.com                                        │
│ 🚀 Hosting:     https://fastmcp.cloud                                        │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Client Connection

### STDIO Client
```
🚀 Starting unified MCP client with STDIO transport

✅ Connected to MCP server via STDIO

📦 Available tools:
  - add: Add two numbers together
  - multiply: Multiply two numbers
  - greet: Greet someone by name

🔢 add(10, 5) = 15
🔢 multiply(10, 5) = 50
👋 greet('FastMCP') = Hello, FastMCP!

📚 Available resources:
  - config://app: get_config
  - config://version: get_version

⚙️  config://app = App configuration data
⚙️  config://version = 1.0.0
```

### SSE Client
```
🚀 Starting unified MCP client with SSE transport

✅ Connected to MCP server via SSE

📦 Available tools:
  - add: Add two numbers together
  - multiply: Multiply two numbers
  - greet: Greet someone by name

🔢 add(10, 5) = 15
🔢 multiply(10, 5) = 50
👋 greet('FastMCP') = Hello, FastMCP!

📚 Available resources:
  - config://app: get_config
  - config://version: get_version

⚙️  config://app = App configuration data
⚙️  config://version = 1.0.0
```

## Multiple Clients Demo

```
======================================================================
🚀 Multiple Clients Demo
======================================================================

This demo shows multiple clients connecting simultaneously.
Note: Make sure the multi-transport server is running!
Run: python run_multi_server.py
======================================================================

[Client 1] Starting with SSE transport...
[Client 2] Starting with SSE transport...
[Client 3] Starting with SSE transport...
[Client 4] Starting with STDIO transport...
[Client 5] Starting with STDIO transport...
[Client 1] ✅ Connected via SSE
[Client 2] ✅ Connected via SSE
[Client 3] ✅ Connected via SSE
[Client 2] 📞 Result: Hello, Client-2!
[Client 3] 📞 Result: Hello, Client-3!
[Client 1] 📞 Result: Hello, Client-1!
[Client 2] ✅ Disconnected
[Client 3] ✅ Disconnected
[Client 1] ✅ Disconnected
[Client 4] ✅ Connected via STDIO
[Client 5] ✅ Connected via STDIO
[Client 4] 📞 Result: Hello, Client-4!
[Client 5] 📞 Result: Hello, Client-5!
[Client 4] ✅ Disconnected
[Client 5] ✅ Disconnected

======================================================================
✅ All clients completed!
======================================================================
```

## Project Structure

```
mcp_project/
├── .github/
│   └── workflows/
│       └── test.yml              # CI/CD pipeline
├── docs/
│   └── SCREENSHOTS.md            # This file
├── examples/
│   ├── multiple_clients.py       # Multiple clients demo
│   ├── use_unified_client.py     # Basic usage example
│   └── README.md                 # Examples documentation
├── src/
│   ├── client/
│   │   ├── unified_client.py     # 🎯 Unified client
│   │   ├── stdio_client.py       # STDIO client
│   │   ├── sse_client.py         # SSE client
│   │   └── http_client.py        # HTTP client
│   └── server/
│       ├── base_server.py        # Core server logic
│       ├── stdio_server.py       # STDIO server
│       └── sse_server.py         # SSE server
├── run_client.py                 # 🎯 Main client entry point
├── run_multi_server.py           # Multi-transport server
├── run_sse_server.py             # SSE server
├── run_http_server.py            # HTTP server
├── run_stdio_server.py           # STDIO server
├── ARCHITECTURE.md               # Architecture documentation
├── TRANSPORTS.md                 # Transport comparison
├── MULTIPLE_CLIENTS.md           # Multiple clients guide
├── GETTING_STARTED.md            # Quick start guide
├── CONTRIBUTING.md               # Contribution guidelines
├── CHANGELOG.md                  # Version history
├── LICENSE                       # MIT License
├── README.md                     # Main documentation
└── requirements.txt              # Python dependencies
```
