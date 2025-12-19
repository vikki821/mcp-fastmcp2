"""
Base MCP Server with all tools and resources
"""
from fastmcp import FastMCP


def create_server(name: str = "Demo Server") -> FastMCP:
    """Create and configure the MCP server"""
    mcp = FastMCP(name)

    @mcp.tool()
    def add(a: int, b: int) -> int:
        """Add two numbers together"""
        return a + b

    @mcp.tool()
    def multiply(a: int, b: int) -> int:
        """Multiply two numbers"""
        return a * b

    @mcp.tool()
    def greet(name: str) -> str:
        """Greet someone by name"""
        return f"Hello, {name}!"

    @mcp.resource("config://app")
    def get_config() -> str:
        """Get application configuration"""
        return "App configuration data"

    @mcp.resource("config://version")
    def get_version() -> str:
        """Get server version"""
        return "1.0.0"

    return mcp
