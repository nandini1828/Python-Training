from __future__ import annotations

from json_query_engine.json_utils import JsonQueryEngine


def run_json_demo() -> None:
    """Show simple nested JSON querying for beginners."""

    payload = {"user": {"profile": {"name": "Ada"}}}
    engine = JsonQueryEngine(payload)
    print("Name:", engine.get_value("user.profile.name"))
    print("Missing value:", engine.get_value("user.profile.age"))
