"""
MCP Client using HTTP transport (streamable-http)
"""
import asyncio
import httpx
from mcp import ClientSession
from mcp.client.sse import sse_client


async def main(url: str = "http://127.0.0.1:8000/mcp"):
    """Connect to MCP server via HTTP"""
    # Note: streamable-http in FastMCP uses SSE under the hood
    # The /mcp endpoint redirects to SSE
    sse_url = url.replace("/mcp", "/sse")
    
    async with sse_client(sse_url) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("✅ Connected to MCP server via HTTP\n")

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


if __name__ == "__main__":
    asyncio.run(main())
