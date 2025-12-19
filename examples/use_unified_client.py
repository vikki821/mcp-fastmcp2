"""
Example: Using the Unified MCP Client programmatically
"""
import sys
import asyncio
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.client.unified_client import MCPClient


async def example_stdio():
    """Example using STDIO transport"""
    print("=" * 60)
    print("Example 1: STDIO Transport")
    print("=" * 60)

    client = MCPClient(transport="stdio")
    await client.run()


async def example_sse():
    """Example using SSE transport"""
    print("\n" + "=" * 60)
    print("Example 2: SSE Transport")
    print("=" * 60)
    print("Note: Make sure SSE server is running!")
    print("Run: python run_sse_server.py")
    print("=" * 60 + "\n")

    try:
        client = MCPClient(transport="sse")
        await client.run(url="http://127.0.0.1:8000/sse")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure the SSE server is running first!")


async def main():
    """Run all examples"""
    # Example 1: STDIO (always works)
    await example_stdio()

    # Example 2: SSE (requires server to be running)
    await example_sse()


if __name__ == "__main__":
    asyncio.run(main())
