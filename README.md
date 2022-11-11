# Core Algorithms & Data Structures Toolkit ⚡

A production-grade Python library providing optimized data structures, thread-safe concurrency primitives, and graph traversal algorithms with zero external dependencies.

[![CI](https://github.com/status/ci.svg)](https://github.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)

## 📂 Modules
- **`algorithms/cache/`**: Thread-safe LRU cache with TTL eviction policies.
- **`algorithms/graphs/`**: Min-heap Dijkstra shortest-path and cycle detection.
- **`algorithms/trees/`**: Prefix Tree (Trie) supporting wildcard pattern searches.
- **`utils/concurrency/`**: Token bucket rate limiters and exponential backoff retry decorators.

## 🧪 Testing & Verification
```bash
pytest tests/ -v
```
