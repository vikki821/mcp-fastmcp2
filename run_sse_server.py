"""
Run MCP Server with SSE transport
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.server.base_server import create_server


if __name__ == "__main__":
    mcp = create_server("MCP Server (SSE)")
    print("Starting SSE server on http://127.0.0.1:8000/sse")
    mcp.run(transport="sse", host="127.0.0.1", port=8000)
