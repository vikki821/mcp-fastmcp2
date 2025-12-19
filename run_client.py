"""
Unified MCP Client Runner
Supports both STDIO and SSE transports
"""
import sys
import asyncio
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.client.unified_client import main


if __name__ == "__main__":
    # Parse command line arguments
    if len(sys.argv) < 2:
        print("Usage: python run_client.py [stdio|sse|http] [options]")
        print("\nExamples:")
        print("  python run_client.py stdio")
        print("  python run_client.py sse")
        print("  python run_client.py http")
        print("  python run_client.py sse --url http://localhost:8000/sse")
        sys.exit(1)

    transport = sys.argv[1]

    if transport not in ["stdio", "sse", "http"]:
        print(f"Error: Invalid transport '{transport}'")
        print("Valid transports: stdio, sse, http")
        sys.exit(1)

    # Parse additional options
    kwargs = {}
    if transport == "sse" and "--url" in sys.argv:
        url_index = sys.argv.index("--url")
        if url_index + 1 < len(sys.argv):
            kwargs["url"] = sys.argv[url_index + 1]

    print(f"🚀 Starting unified MCP client with {transport.upper()} transport\n")
    asyncio.run(main(transport=transport, **kwargs))
