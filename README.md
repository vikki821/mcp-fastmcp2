# MCP Server and Client with FastMCP2

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.0%2B-green.svg)](https://gofastmcp.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A complete, production-ready implementation of the Model Context Protocol (MCP) with a unified client supporting multiple transport methods.

## ✨ Features

- 🎯 **Unified Client** - One client for all transports (STDIO, SSE, HTTP)
- 🚀 **Multiple Transports** - STDIO, SSE, and HTTP support
- 🔄 **Concurrent Clients** - Multiple clients can connect simultaneously
- 📦 **Ready-to-Use Tools** - Add, multiply, greet functions included
- 📚 **Resource Management** - Config and version resources
- 🏗️ **Clean Architecture** - Modular, extensible, well-documented
- 🔒 **Type Safe** - Full type hints throughout
- ⚡ **Async/Await** - Modern async Python patterns

## Project Structure

```
mcp_project/
├── .venv/                       # Virtual environment
├── src/
│   ├── __init__.py
│   ├── server/
│   │   ├── __init__.py
│   │   ├── base_server.py      # Core server with tools & resources
│   │   ├── sse_server.py        # SSE transport server (unused)
│   │   └── stdio_server.py      # STDIO transport server (unused)
│   └── client/
│       ├── __init__.py
│       ├── unified_client.py    # 🎯 Unified client (both transports)
│       ├── sse_client.py        # SSE transport client
│       └── stdio_client.py      # STDIO transport client
├── run_client.py                # 🎯 Unified client (RECOMMENDED)
├── run_sse_server.py            # ✅ Run SSE server
├── run_stdio_server.py          # ✅ Run STDIO server
├── run_sse_client.py            # ✅ Run SSE client (individual)
├── run_stdio_client.py          # ✅ Run STDIO client (individual)
├── requirements.txt
└── README.md
```

## Features

### Server Tools
- `add(a, b)` - Add two numbers
- `multiply(a, b)` - Multiply two numbers
- `greet(name)` - Greet someone by name

### Server Resources
- `config://app` - Application configuration
- `config://version` - Server version

## Transport Methods

### 🎯 Unified Client (Recommended)
One client that supports both transports!

**STDIO Transport:**
```bash
python run_client.py stdio
```

**SSE Transport:**
```bash
# Start SSE server first
python run_sse_server.py

# Then run client
python run_client.py sse
```

**Custom SSE URL:**
```bash
python run_client.py sse --url http://localhost:8000/sse
```

### 1. SSE (Server-Sent Events)
HTTP-based transport for web applications and remote clients.

**Start SSE Server:**
```bash
python run_sse_server.py
```
Server runs on: `http://127.0.0.1:8000/sse`

**Run SSE Client (individual):**
```bash
python run_sse_client.py
```

### 2. STDIO (Standard Input/Output)
Process-based transport for local integrations.

**Run STDIO Client (individual, auto-starts server):**
```bash
python run_stdio_client.py
```

## Quick Start

### Test STDIO (Easiest)
```bash
python run_client.py stdio
```
This automatically starts the server and connects!

### Test Multiple Transports (Recommended)
```bash
# Terminal 1: Start multi-transport server
python run_multi_server.py

# Terminal 2: Connect with SSE
python run_client.py sse

# Terminal 3: Connect with another SSE client
python run_client.py sse

# Multiple clients can connect simultaneously!
```

### Test STDIO (Separate Instances)
```bash
python run_client.py stdio
```

## Setup

1. Create virtual environment:
```bash
python -m venv .venv
```

2. Activate virtual environment:
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage Examples

### SSE Transport
```python
from src.client.sse_client import main
import asyncio

# Connect to SSE server
asyncio.run(main("http://127.0.0.1:8000/sse"))
```

### STDIO Transport
```python
from src.client.stdio_client import main
import asyncio

# Connect via STDIO
asyncio.run(main())
```

## Development

The project uses FastMCP2 for easy MCP server/client implementation:
- Decorator-based tool registration
- Automatic schema generation
- Multiple transport support
- Type-safe tool definitions

## Documentation

- FastMCP: https://gofastmcp.com
- MCP Specification: https://modelcontextprotocol.io
