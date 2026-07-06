"""List utilities demonstrating common list operations.
"""

from typing import Any, Iterable, List
import logging

logger = logging.getLogger(__name__)


def unique(items: Iterable[Any]) -> List[Any]:
    """Return list of unique items preserving order."""

    seen = set()
    result: List[Any] = []
    for it in items:
        if it in seen:
            continue
        seen.add(it)
        result.append(it)
    logger.debug("unique result length=%d", len(result))
    return result


def chunk(items: List[Any], size: int) -> List[List[Any]]:
    """Split a list into chunks of given size."""

    if size <= 0:
        raise ValueError("size must be > 0")
    return [items[i : i + size] for i in range(0, len(items), size)]
