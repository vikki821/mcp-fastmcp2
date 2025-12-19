"""
Unified MCP Client supporting multiple transports
"""
import asyncio
from typing import Literal
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.sse import sse_client
import httpx


class MCPClient:
    """Unified MCP Client that supports multiple transports"""

    def __init__(self, transport: Literal["stdio", "sse", "http"] = "stdio"):
        self.transport = transport
        self.session = None

    async def connect_stdio(self, command: str = ".venv/Scripts/python.exe", args: list = None):
        """Connect using STDIO transport"""
        if args is None:
            args = ["run_stdio_server.py"]

        server_params = StdioServerParameters(command=command, args=args)
        return stdio_client(server_params)

    async def connect_sse(self, url: str = "http://127.0.0.1:8000/sse"):
        """Connect using SSE transport"""
        return sse_client(url)

    async def connect_http(self, url: str = "http://127.0.0.1:8000"):
        """Connect using HTTP transport (streamable-http)"""
        # For streamable-http, we use httpx directly
        from contextlib import asynccontextmanager
        
        @asynccontextmanager
        async def http_connection():
            async with httpx.AsyncClient() as client:
                # Create read/write streams for HTTP
                from mcp.client.session import ClientSession
                from mcp.shared.memory import create_connected_server_and_client_session
                
                # Use SSE client as fallback for now
                # Full HTTP implementation would require custom stream handling
                async with sse_client(f"{url}/sse") as streams:
                    yield streams
        
        return http_connection()

    async def run(self, **kwargs):
        """Run the client with specified transport"""
        # Select transport
        if self.transport == "stdio":
            connection = await self.connect_stdio(**kwargs)
        elif self.transport == "sse":
            url = kwargs.get("url", "http://127.0.0.1:8000/sse")
            connection = await self.connect_sse(url)
        elif self.transport == "http":
            url = kwargs.get("url", "http://127.0.0.1:8000")
            connection = await self.connect_http(url)
        else:
            raise ValueError(f"Unsupported transport: {self.transport}")

        # Connect and interact
        async with connection as (read, write):
            async with ClientSession(read, write) as session:
                self.session = session
                await session.initialize()

                print(f"✅ Connected to MCP server via {self.transport.upper()}\n")

                # List available tools
                tools = await session.list_tools()
                print("📦 Available tools:")
                for tool in tools.tools:
                    print(f"  - {tool.name}: {tool.description}")

                # Call tools
                result = await session.call_tool("add", arguments={"a": 10, "b": 5})
                print(f"\n🔢 add(10, 5) = {result.content[0].text}")

                result = await session.call_tool("multiply", arguments={"a": 10, "b": 5})
                print(f"🔢 multiply(10, 5) = {result.content[0].text}")

                result = await session.call_tool("greet", arguments={"name": "FastMCP"})
                print(f"👋 greet('FastMCP') = {result.content[0].text}")

                # List resources
                resources = await session.list_resources()
                print(f"\n📚 Available resources:")
                for resource in resources.resources:
                    print(f"  - {resource.uri}: {resource.name}")

                # Read resources
                config = await session.read_resource("config://app")
                print(f"\n⚙️  config://app = {config.contents[0].text}")

                version = await session.read_resource("config://version")
                print(f"⚙️  config://version = {version.contents[0].text}")


async def main(transport: Literal["stdio", "sse", "http"] = "stdio", **kwargs):
    """Main entry point for unified client"""
    client = MCPClient(transport=transport)
    await client.run(**kwargs)


if __name__ == "__main__":
    import sys

    # Parse command line arguments
    transport = sys.argv[1] if len(sys.argv) > 1 else "stdio"

    if transport not in ["stdio", "sse", "http"]:
        print("Usage: python unified_client.py [stdio|sse|http]")
        sys.exit(1)

    print(f"🚀 Starting unified MCP client with {transport.upper()} transport\n")
    asyncio.run(main(transport=transport))
