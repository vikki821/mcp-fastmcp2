"""
Setup configuration for MCP FastMCP2 Project
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mcp-fastmcp2",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Complete MCP implementation with unified client supporting multiple transports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mcp-fastmcp2",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.10",
    install_requires=[
        "fastmcp>=2.0.0",
    ],
    entry_points={
        "console_scripts": [
            "mcp-client=run_client:main",
            "mcp-server=run_multi_server:main",
        ],
    },
)
