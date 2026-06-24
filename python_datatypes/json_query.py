from __future__ import annotations

import logging
import re
from typing import Any, Iterable, List, Optional, Union

from .logging_config import configure_logging

logger = configure_logging()

PathType = Union[str, int, Iterable[Union[str, int]]]
_TOKEN_PATTERN = re.compile(r"\[([^\]]+)\]|([^.\[\]]+)")


def _parse_path(path: str) -> List[Union[str, int]]:
    segments: List[Union[str, int]] = []
    for match in _TOKEN_PATTERN.finditer(path):
        token = match.group(1) if match.group(1) is not None else match.group(2)
        if token is None:
            continue
        token = token.strip()
        if token.isdigit():
            segments.append(int(token))
        else:
            segments.append(token)
    return segments


def _normalize_path(path: PathType) -> List[Union[str, int]]:
    if isinstance(path, str):
        return _parse_path(path)
    if isinstance(path, int):
        return [path]
    if isinstance(path, Iterable):
        normalized: List[Union[str, int]] = []
        for token in path:
            if isinstance(token, (str, int)):
                normalized.append(int(token) if isinstance(token, str) and token.isdigit() else token)
        return normalized
    return []


def resolve_json_path(data: Any, path: PathType) -> Any:
    logger.info("Resolving JSON path %s against input data", path)
    if data is None or path is None:
        return None

    tokens = _normalize_path(path)
    current: Any = data

    for token in tokens:
        if isinstance(current, dict):
            current = current.get(token)
        elif isinstance(current, (list, tuple)) and isinstance(token, int):
            if 0 <= token < len(current):
                current = current[token]
            else:
                return None
        elif hasattr(current, str(token)):
            try:
                current = getattr(current, str(token))
            except Exception:
                return None
        else:
            return None

        if current is None:
            return None

    return current
