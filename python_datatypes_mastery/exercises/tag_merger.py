"""
Tag merging utility using set operations.
"""
from __future__ import annotations

from typing import Iterable, Set, Tuple, List


def merge_tags(tags_a: Iterable[str], tags_b: Iterable[str]) -> Tuple[Set[str], Set[str], Set[str]]:
    """
    Merge two tag collections.

    Args:
        tags_a: First iterable of tags.
        tags_b: Second iterable of tags.

    Returns:
        A tuple (all_unique, shared, only_in_first), all sets of lowercase tags.
    """
    a = {t.strip().lower() for t in tags_a}
    b = {t.strip().lower() for t in tags_b}
    all_unique = a.union(b)
    shared = a.intersection(b)
    only_in_first = a.difference(b)
    return all_unique, shared, only_in_first
