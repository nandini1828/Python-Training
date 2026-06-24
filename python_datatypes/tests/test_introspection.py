from python_datatypes.introspection import introspect_object


def test_introspect_basic_dict() -> None:
    payload = {"name": "Alice", "score": 10}
    result = introspect_object(payload)

    assert result["type"] == "dict"
    assert "attributes" in result
    assert result["repr"] == "{'name': 'Alice', 'score': 10}"
