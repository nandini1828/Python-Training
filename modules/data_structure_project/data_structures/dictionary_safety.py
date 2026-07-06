"""Safe dictionary access helpers."""

from collections import defaultdict
from typing import DefaultDict, Dict, List, TypeVar

K = TypeVar("K")
V = TypeVar("V")


def safe_lookup(mapping: Dict[K, V], key: K, default: V) -> V:
    """Safely retrieve a value, returning a default when missing."""
    return mapping.get(key, default)


def count_words(words: List[str]) -> DefaultDict[str, int]:
    """Count word frequencies using defaultdict."""
    counts: DefaultDict[str, int] = defaultdict(int)
    for word in words:
        counts[word] += 1
    return counts
