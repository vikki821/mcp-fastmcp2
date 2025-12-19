@echo off
REM Initialize Git repository and prepare for GitHub

echo 🚀 Initializing Git repository...

REM Initialize git if not already initialized
if not exist .git (
    git init
    echo ✅ Git repository initialized
) else (
    echo ℹ️  Git repository already exists
)

REM Add all files
echo 📦 Adding files to git...
git add .

REM Create initial commit
echo 💾 Creating initial commit...
git commit -m "Initial commit: MCP FastMCP2 project with unified client" -m "Features:" -m "- Unified client supporting STDIO, SSE, and HTTP transports" -m "- Multi-transport server" -m "- Example tools and resources" -m "- Comprehensive documentation" -m "- Multiple client support" -m "- Clean, modular architecture"

REM Create main branch if needed
git branch -M main

echo.
echo ✅ Git repository initialized successfully!
echo.
echo 📝 Next steps:
echo 1. Create a new repository on GitHub
echo 2. Run these commands:
echo.
echo    git remote add origin https://github.com/yourusername/mcp-fastmcp2.git
echo    git push -u origin main
echo.
echo 🎉 Done!
pause
