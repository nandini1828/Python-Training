from __future__ import annotations

from json_query_engine.json_utils import JsonQueryEngine


def test_json_query_engine_returns_nested_values() -> None:
    engine = JsonQueryEngine({"user": {"profile": {"name": "Ada"}}})
    assert engine.get_value("user.profile.name") == "Ada"
    assert engine.get_value("user.profile.age") is None
