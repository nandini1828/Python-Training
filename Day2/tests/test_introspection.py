from __future__ import annotations

from introspection.introspection_utils import (
    extract_documentation,
    inspect_object,
    list_available_methods,
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


def test_extract_documentation_for_function() -> None:
    documentation = extract_documentation(len)
    assert documentation["docstring"] is not None


def test_list_available_methods_for_dict() -> None:
    methods = list_available_methods({"a": 1})
    assert "keys" in methods
    assert "values" in methods


def test_inspect_object_supports_custom_instances() -> None:
    class SampleObject:
        def __init__(self) -> None:
            self.name = "Ada"

    result = inspect_object(SampleObject())
    assert result["kind"] == "instance"
    assert "name" in result["attributes"]
