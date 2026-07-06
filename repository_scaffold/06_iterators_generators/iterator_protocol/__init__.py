"""
iterator_protocol

Reusable utilities and demonstrations for Python's iterator protocol.
"""

from .utils import CountDown, collect_iterator, get_first, is_iterable, manual_next

__all__ = [
    "CountDown",
    "is_iterable",
    "get_first",
    "collect_iterator",
    "manual_next",
]
