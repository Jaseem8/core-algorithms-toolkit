"""Tests for LRUCache."""
import time
from algorithms.cache.lru_cache import LRUCache

def test_lru_eviction():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    assert cache.get("a") is None
    assert cache.get("b") == 2
    assert cache.get("c") == 3

def test_lru_ttl():
    cache = LRUCache(2)
    cache.put("k", "v", ttl=0.05)
    assert cache.get("k") == "v"
    time.sleep(0.06)
    assert cache.get("k") is None
