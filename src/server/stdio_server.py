"""
MCP Server with STDIO transport
"""
from .base_server import create_server


def main():
    """Run server with STDIO transport"""
    mcp = create_server("MCP Server (STDIO)")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
