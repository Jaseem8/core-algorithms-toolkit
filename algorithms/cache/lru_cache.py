
# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock

# Optimized node unlinking

# Fine-grained read lock
"""Thread-safe LRU Cache with TTL."""
import time
import threading
from typing import Any, Optional, Dict

class Node:
    def __init__(self, key: Any, value: Any, ttl: Optional[float] = None):
        self.key = key
        self.value = value
        self.expires_at = (time.time() + ttl) if ttl else None
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None
