"""Tests for query_json utility."""
from python_datatypes_mastery.exercises.json_query import query_json


def test_query_exists():
    data = {"a": {"b": {"c": 1}}}
    assert query_json(data, "a.b.c") == 1


def test_query_missing_returns_default():
    data = {"x": 1}
    assert query_json(data, "x.y", default="missing") == "missing"
