# MCP Project Architecture

## Overview

This project implements a complete Model Context Protocol (MCP) server and client system using FastMCP2, supporting multiple transport methods through a unified client interface.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    MCP Client Layer                      │
│  ┌───────────────────────────────────────────────────┐  │
│  │         Unified Client (unified_client.py)        │  │
│  │  - Single interface for all transports            │  │
│  │  - Transport selection via parameter              │  │
│  └───────────────────────────────────────────────────┘  │
│           │                              │               │
│           ▼                              ▼               │
│  ┌─────────────────┐          ┌─────────────────┐      │
│  │  STDIO Client   │          │   SSE Client    │      │
│  │  (stdio_client) │          │  (sse_client)   │      │
│  └─────────────────┘          └─────────────────┘      │
└─────────────────────────────────────────────────────────┘
                    │                      │
                    │                      │
         ┌──────────┴──────────┐          │
         ▼                     ▼          ▼
┌─────────────────┐   ┌─────────────────────────┐
│  STDIO Server   │   │     SSE Server          │
│  (Process I/O)  │   │  (HTTP/SSE on :8000)    │
└─────────────────┘   └─────────────────────────┘
         │                     │
         └──────────┬──────────┘
                    ▼
         ┌─────────────────────┐
         │   Base Server       │
         │  (base_server.py)   │
         │                     │
         │  Tools:             │
         │  - add()            │
         │  - multiply()       │
         │  - greet()          │
         │                     │
         │  Resources:         │
         │  - config://app     │
         │  - config://version │
         └─────────────────────┘
```

## Components

### 1. Base Server (`src/server/base_server.py`)
- **Purpose**: Core server logic shared across all transports
- **Features**:
  - Tool registration using decorators
  - Resource management
  - Type-safe function definitions
- **Tools**:
  - `add(a: int, b: int) -> int`
  - `multiply(a: int, b: int) -> int`
  - `greet(name: str) -> str`
- **Resources**:
  - `config://app` - Application configuration
  - `config://version` - Server version

### 2. Unified Client (`src/client/unified_client.py`)
- **Purpose**: Single client interface supporting multiple transports
- **Key Features**:
  - Transport abstraction
  - Consistent API across transports
  - Easy transport switching
  - Command-line and programmatic usage

### 3. Transport Implementations

#### STDIO Transport
- **Communication**: Standard Input/Output streams
- **Use Cases**:
  - Local development
  - Process-to-process communication
  - IDE integrations (Claude Desktop, Cline)
- **Advantages**:
  - No network overhead
  - Automatic server lifecycle management
  - Secure (local only)

#### SSE Transport
- **Communication**: HTTP with Server-Sent Events
- **Use Cases**:
  - Web applications
  - Remote clients
  - Multi-client scenarios
- **Advantages**:
  - Network accessible
  - Browser compatible
  - Multiple simultaneous connections

## Design Patterns

### 1. Factory Pattern
The `create_server()` function acts as a factory, creating configured server instances:
```python
def create_server(name: str = "Demo Server") -> FastMCP:
    mcp = FastMCP(name)
    # Register tools and resources
    return mcp
```

### 2. Strategy Pattern
The unified client uses strategy pattern for transport selection:
```python
class MCPClient:
    def __init__(self, transport: Literal["stdio", "sse"]):
        self.transport = transport
    
    async def run(self, **kwargs):
        if self.transport == "stdio":
            connection = await self.connect_stdio(**kwargs)
        elif self.transport == "sse":
            connection = await self.connect_sse(**kwargs)
```

### 3. Decorator Pattern
FastMCP uses decorators for tool and resource registration:
```python
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.resource("config://app")
def get_config() -> str:
    return "App configuration data"
```

## Data Flow

### STDIO Flow
```
Client Request → STDIO → Server Process → Tool Execution → Response → STDIO → Client
```

### SSE Flow
```
Client Request → HTTP POST → SSE Server → Tool Execution → Response → SSE Stream → Client
```

## Key Benefits

1. **Unified Interface**: One client for all transports
2. **Modular Design**: Easy to add new transports
3. **Type Safety**: Full type hints throughout
4. **Async/Await**: Modern async Python patterns
5. **Testability**: Clear separation of concerns
6. **Extensibility**: Easy to add new tools and resources

## Usage Patterns

### Quick Test (STDIO)
```bash
python run_client.py stdio
```

### Production (SSE)
```bash
# Terminal 1
python run_sse_server.py

# Terminal 2
python run_client.py sse
```

### Programmatic
```python
from src.client.unified_client import MCPClient

client = MCPClient(transport="stdio")
await client.run()
```

## Future Enhancements

Potential additions:
- WebSocket transport
- gRPC transport
- Authentication/Authorization
- Rate limiting
- Logging and monitoring
- Tool versioning
- Resource caching
- Connection pooling
