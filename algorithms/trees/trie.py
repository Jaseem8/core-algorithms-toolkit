"""Prefix Tree (Trie)."""
from typing import Dict, Optional

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end: bool = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, pattern: str) -> bool:
        def _match(idx: int, node: TrieNode) -> bool:
            if idx == len(pattern):
                return node.is_end
            ch = pattern[idx]
            if ch == ".":
                return any(_match(idx + 1, child) for child in node.children.values())
            if ch not in node.children:
                return False
            return _match(idx + 1, node.children[ch])
        return _match(0, self.root)
