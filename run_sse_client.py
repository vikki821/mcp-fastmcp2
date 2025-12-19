"""
Run MCP Client with SSE transport
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.client.sse_client import main
import asyncio


if __name__ == "__main__":
    asyncio.run(main())
