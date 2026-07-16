"""JSON utility helpers for reading and writing data files."""

import json
from pathlib import Path


def load_json(file_path: str | Path) -> list[dict[str, object]]:
    """Read JSON content from a file path."""
    with Path(file_path).open("r", encoding="utf-8") as file:
        return json.load(file)


def save_json(file_path: str | Path, data: list[dict[str, object]]) -> None:
    """Write JSON content to a file path."""
    with Path(file_path).open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
