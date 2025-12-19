"""
MCP Server using FastMCP2
"""
from fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Demo Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b


@mcp.tool()
def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello, {name}!"


@mcp.resource("config://app")
def get_config() -> str:
    """Get application configuration"""
    return "App configuration data"


if __name__ == "__main__":
    mcp.run(transport="sse")
