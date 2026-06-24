from __future__ import annotations

from introspection.introspection_utils import (
    extract_documentation,
    inspect_object,
    list_available_methods,
    query_json,
)


def test_inspect_builtin_list() -> None:
    result = inspect_object([1, 2, 3])
    assert result["kind"] == "list"
    assert result["is_callable"] is False
    assert "append" in result["methods"]


def test_inspect_function() -> None:
    result = inspect_object(len)
    assert result["kind"] == "function"
    assert result["is_callable"] is True
    assert "__name__" in result["attributes"]


def test_inspect_object_returns_methods_with_documentation() -> None:
    result = inspect_object([1, 2, 3])
    assert "append" in result["methods_with_docs"]
    assert result["methods_with_docs"]["append"] is not None


def test_extract_documentation_for_function() -> None:
    documentation = extract_documentation(len)
    assert documentation["docstring"] is not None
    assert documentation["module_docstring"] is not None


def test_list_available_methods_for_dict() -> None:
    methods = list_available_methods({"a": 1})
    assert "keys" in methods
    assert "values" in methods


def test_query_json_supports_nested_paths() -> None:
    payload = {"user": {"profile": {"name": "Ada"}}}
    assert query_json(payload, "user.profile.name") == "Ada"
    assert query_json(payload, "user.profile.age") is None
    assert query_json(payload, ["user", "profile", "name"]) == "Ada"
