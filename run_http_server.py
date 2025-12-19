"""
Run MCP Server with Streamable HTTP transport
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.server.base_server import create_server


if __name__ == "__main__":
    mcp = create_server("MCP Server (HTTP)")
    print("Starting HTTP server on http://127.0.0.1:8000")
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)
