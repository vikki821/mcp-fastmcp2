#!/bin/bash
# Initialize Git repository and prepare for GitHub

echo "🚀 Initializing Git repository..."

# Initialize git if not already initialized
if [ ! -d .git ]; then
    git init
    echo "✅ Git repository initialized"
else
    echo "ℹ️  Git repository already exists"
fi

# Add all files
echo "📦 Adding files to git..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: MCP FastMCP2 project with unified client

Features:
- Unified client supporting STDIO, SSE, and HTTP transports
- Multi-transport server
- Example tools and resources
- Comprehensive documentation
- Multiple client support
- Clean, modular architecture"

# Create main branch if needed
git branch -M main

echo ""
echo "✅ Git repository initialized successfully!"
echo ""
echo "📝 Next steps:"
echo "1. Create a new repository on GitHub"
echo "2. Run these commands:"
echo ""
echo "   git remote add origin https://github.com/yourusername/mcp-fastmcp2.git"
echo "   git push -u origin main"
echo ""
echo "🎉 Done!"
