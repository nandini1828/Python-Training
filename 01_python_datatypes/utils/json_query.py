"""utils.json_query
====================
Nested JSON / dict/list query utilities.
"""

from typing import Any, Dict
import logging

logger = logging.getLogger(__name__)


def query_json(data: Dict[str, Any], path: str) -> Any:
    """Safely query nested structures using dotted paths.

    Supports dictionary keys and list indexes (numeric segments).

    Examples:
        query_json(data, "user.name")
        query_json(data, "employees.0.name")

    Returns None when path cannot be resolved.
    """

    logger.debug("Querying JSON path: %s", path)

    if not path:
        return None

    current: Any = data

    for part in path.split("."):
        if current is None:
            return None

        # list index
        if isinstance(current, list):
            try:
                idx = int(part)
            except (ValueError, TypeError):
                return None
            if idx < 0 or idx >= len(current):
                return None
            current = current[idx]
            continue

        # dict key
        if isinstance(current, dict):
            if part in current:
                current = current[part]
                continue
            else:
                # support numeric keys as strings
                if part.isdigit() and part in current:
                    current = current[part]
                    continue
                return None

        # object with attribute
        if hasattr(current, part):
            try:
                current = getattr(current, part)
                continue
            except Exception:
                return None

        return None

    logger.info("JSON query complete: %s -> %s", path, type(current))
    return current
