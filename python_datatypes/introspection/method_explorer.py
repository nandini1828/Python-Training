from __future__ import annotations

import logging
from typing import Any, List

from ..logging_config import configure_logging

logger = configure_logging()


def explore_methods(obj: Any, include_dunder: bool = False) -> List[str]:
    logger.info("Exploring methods for object type %s", type(obj).__name__)
    method_names: List[str] = []
    for name in dir(obj):
        if not include_dunder and name.startswith("__") and name.endswith("__"):
            continue
        attribute = getattr(obj, name, None)
        if callable(attribute):
            method_names.append(name)
    return sorted(set(method_names))
