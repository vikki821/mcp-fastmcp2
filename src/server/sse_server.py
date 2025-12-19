"""
MCP Server with SSE transport
"""
from .base_server import create_server


def main(host: str = "127.0.0.1", port: int = 8000):
    """Run server with SSE transport"""
    mcp = create_server("MCP Server (SSE)")
    mcp.run(transport="sse", host=host, port=port)


if __name__ == "__main__":
    main()
