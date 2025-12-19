"""
MCP Client using FastMCP2 with SSE transport
"""
import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client


async def main():
    # Connect to SSE server
    url = "http://127.0.0.1:8000/sse"
    
    async with sse_client(url) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            
            print("✅ Connected to MCP server via SSE\n")
            
            # List available tools
            tools = await session.list_tools()
            print("📦 Available tools:")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")
            
            # Call the add tool
            result = await session.call_tool("add", arguments={"a": 5, "b": 3})
            print(f"\n🔢 Calling add(5, 3): {result.content[0].text}")
            
            # Call the greet tool
            result = await session.call_tool("greet", arguments={"name": "World"})
            print(f"👋 Calling greet('World'): {result.content[0].text}")
            
            # List resources
            resources = await session.list_resources()
            print(f"\n📚 Available resources:")
            for resource in resources.resources:
                print(f"  - {resource.uri}: {resource.name}")
            
            # Read a resource
            resource_content = await session.read_resource("config://app")
            print(f"\n⚙️  Reading config://app: {resource_content.contents[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
