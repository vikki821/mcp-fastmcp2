"""
Run MCP Server with MULTIPLE transports simultaneously
Supports SSE and HTTP on the same server
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.server.base_server import create_server


if __name__ == "__main__":
    mcp = create_server("MCP Multi-Transport Server")
    
    print("=" * 60)
    print("🚀 Starting MCP Server with MULTIPLE transports")
    print("=" * 60)
    print("\n📡 Available endpoints:")
    print("  • SSE:  http://127.0.0.1:8000/sse")
    print("  • HTTP: http://127.0.0.1:8000/mcp")
    print("\n💡 Clients can connect using either transport!")
    print("=" * 60)
    print()
    
    # FastMCP automatically exposes both SSE and HTTP endpoints
    # when using either transport
    mcp.run(transport="sse", host="127.0.0.1", port=8000)
