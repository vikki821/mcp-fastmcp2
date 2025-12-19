"""
Run MCP Server with STDIO transport
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.server.base_server import create_server


if __name__ == "__main__":
    mcp = create_server("MCP Server (STDIO)")
    mcp.run(transport="stdio")
