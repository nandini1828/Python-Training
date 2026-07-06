"""Set utilities: reusable operations demonstrating set behavior."""

from typing import Iterable, Set
import logging

logger = logging.getLogger(__name__)


def union(a: Iterable[str], b: Iterable[str]) -> Set[str]:
    """Return the union of two iterables as a set."""

    result = set(a) | set(b)
    logger.debug("union sizes: %d, %d -> %d", len(set(a)), len(set(b)), len(result))
    return result


def intersection(a: Iterable[str], b: Iterable[str]) -> Set[str]:
    """Return intersection of two iterables."""

    result = set(a) & set(b)
    logger.debug("intersection size=%d", len(result))
    return result


def is_subset(a: Iterable[str], b: Iterable[str]) -> bool:
    """Return True if set(a) is subset of set(b)."""

    return set(a) <= set(b)
