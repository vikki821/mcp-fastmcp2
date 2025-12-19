# Contributing to MCP FastMCP2 Project

Thank you for your interest in contributing! 🎉

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](../../issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment (OS, Python version)

### Suggesting Features

1. Check [Issues](../../issues) for existing feature requests
2. Create a new issue with:
   - Clear description of the feature
   - Use cases and benefits
   - Possible implementation approach

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes thoroughly
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/mcp-fastmcp2.git
cd mcp-fastmcp2

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python run_client.py stdio
```

## Code Style

- Follow PEP 8 guidelines
- Use type hints
- Add docstrings to functions and classes
- Keep functions focused and small
- Write descriptive variable names

## Testing

Before submitting a PR:

1. Test all transports:
   ```bash
   python run_client.py stdio
   python run_client.py sse
   python run_client.py http
   ```

2. Test multiple clients:
   ```bash
   python run_multi_server.py
   python examples/multiple_clients.py
   ```

3. Verify documentation is up to date

## Adding New Features

### Adding a New Tool

Edit `src/server/base_server.py`:

```python
@mcp.tool()
def your_tool(param: str) -> str:
    """Your tool description"""
    return f"Result: {param}"
```

### Adding a New Resource

Edit `src/server/base_server.py`:

```python
@mcp.resource("myapp://data")
def get_data() -> str:
    """Get application data"""
    return "Your data here"
```

### Adding a New Transport

1. Create client in `src/client/`
2. Update `unified_client.py`
3. Add runner script
4. Update documentation

## Documentation

When adding features:

1. Update README.md
2. Update relevant .md files
3. Add examples if applicable
4. Update docstrings

## Questions?

Feel free to:
- Open an issue for discussion
- Ask in pull request comments
- Check existing documentation

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn and grow

Thank you for contributing! 🚀
