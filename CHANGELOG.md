# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-19

### Added
- Initial release
- Unified MCP client supporting multiple transports
- STDIO transport implementation
- SSE (Server-Sent Events) transport implementation
- HTTP (Streamable-HTTP) transport implementation
- Multi-transport server supporting SSE and HTTP simultaneously
- Example tools: add, multiply, greet
- Example resources: config://app, config://version
- Comprehensive documentation:
  - README.md - Main documentation
  - GETTING_STARTED.md - Quick start guide
  - ARCHITECTURE.md - Design and architecture
  - TRANSPORTS.md - Transport comparison
  - MULTIPLE_CLIENTS.md - Multiple client guide
  - CONTRIBUTING.md - Contribution guidelines
- Examples:
  - use_unified_client.py - Basic usage
  - multiple_clients.py - Concurrent clients demo
- GitHub Actions CI/CD workflow
- MIT License

### Features
- Single unified client for all transports
- Command-line interface: `python run_client.py [stdio|sse|http]`
- Programmatic API for custom integrations
- Support for multiple concurrent clients
- Clean, modular architecture
- Type-safe implementation with full type hints
- Async/await throughout

### Documentation
- Complete API documentation
- Usage examples
- Architecture diagrams
- Transport comparison tables
- Best practices guide

## [Unreleased]

### Planned
- WebSocket transport (when FastMCP adds support)
- Authentication middleware
- Rate limiting
- Connection pooling
- Monitoring and metrics
- Docker support
- Kubernetes deployment examples
