"""
Example: Multiple clients connecting simultaneously to the same server
Demonstrates that multiple clients can connect at the same time
"""
import sys
import asyncio
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.client.unified_client import MCPClient


async def client_task(client_id: int, transport: str):
    """Run a client task"""
    print(f"[Client {client_id}] Starting with {transport.upper()} transport...")
    
    try:
        client = MCPClient(transport=transport)
        
        # For demo, we'll just connect and call one tool
        if transport == "stdio":
            # STDIO creates its own server instance
            connection = await client.connect_stdio()
        else:
            # SSE connects to shared server
            connection = await client.connect_sse()
        
        async with connection as (read, write):
            from mcp import ClientSession
            async with ClientSession(read, write) as session:
                await session.initialize()
                
                print(f"[Client {client_id}] ✅ Connected via {transport.upper()}")
                
                # Call a tool
                result = await session.call_tool("greet", arguments={"name": f"Client-{client_id}"})
                print(f"[Client {client_id}] 📞 Result: {result.content[0].text}")
                
                # Small delay to show concurrent execution
                await asyncio.sleep(1)
                
                print(f"[Client {client_id}] ✅ Disconnected")
    
    except Exception as e:
        print(f"[Client {client_id}] ❌ Error: {e}")


async def main():
    """Run multiple clients simultaneously"""
    print("=" * 70)
    print("🚀 Multiple Clients Demo")
    print("=" * 70)
    print("\nThis demo shows multiple clients connecting simultaneously.")
    print("Note: Make sure the multi-transport server is running!")
    print("Run: python run_multi_server.py")
    print("=" * 70)
    print()
    
    # Create multiple client tasks
    tasks = [
        client_task(1, "sse"),
        client_task(2, "sse"),
        client_task(3, "sse"),
        client_task(4, "stdio"),  # STDIO creates its own server
        client_task(5, "stdio"),  # Another STDIO with its own server
    ]
    
    # Run all clients concurrently
    await asyncio.gather(*tasks)
    
    print("\n" + "=" * 70)
    print("✅ All clients completed!")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())
