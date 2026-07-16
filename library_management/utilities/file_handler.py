import json
from pathlib import Path

from utilities.constants import BOOKS_FILE, MEMBERS_FILE


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _resolve_path(relative_path: str) -> Path:
    if Path(relative_path).is_absolute():
        return Path(relative_path)
    return PROJECT_ROOT / relative_path


def load_json(relative_path: str):
    path = _resolve_path(relative_path)
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_json(relative_path: str, payload) -> None:
    path = _resolve_path(relative_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)


def load_books() -> list:
    return load_json(BOOKS_FILE)


def load_members() -> list:
    return load_json(MEMBERS_FILE)


def save_books(payload) -> None:
    save_json(BOOKS_FILE, payload)


def save_members(payload) -> None:
    save_json(MEMBERS_FILE, payload)
