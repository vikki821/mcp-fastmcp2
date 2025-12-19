"""
MCP Client using FastMCP2
"""
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    # Create server parameters for stdio connection
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            
            # List available tools
            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")
            
            # Call the add tool
            result = await session.call_tool("add", arguments={"a": 5, "b": 3})
            print(f"\nCalling add(5, 3): {result.content[0].text}")
            
            # Call the greet tool
            result = await session.call_tool("greet", arguments={"name": "World"})
            print(f"Calling greet('World'): {result.content[0].text}")
            
            # List resources
            resources = await session.list_resources()
            print(f"\nAvailable resources:")
            for resource in resources.resources:
                print(f"  - {resource.uri}: {resource.name}")
            
            # Read a resource
            resource_content = await session.read_resource("config://app")
            print(f"\nReading config://app: {resource_content.contents[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
