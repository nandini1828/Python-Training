"""Tuple utilities: small helpers for tuple analysis."""

from typing import Iterable, List, Tuple
import logging

logger = logging.getLogger(__name__)


def to_list(t: Tuple) -> List:
    """Convert tuple to list."""

    return list(t)


def count_value(t: Tuple, value: object) -> int:
    """Count occurrences of value in tuple."""

    c = t.count(value)
    logger.debug("count_value %s -> %d", value, c)
    return c
