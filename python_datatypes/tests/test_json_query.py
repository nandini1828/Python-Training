from python_datatypes.json_query import resolve_json_path


def test_resolve_json_path_nested_dict() -> None:
    data = {"user": {"profile": {"id": 123, "name": "Dana"}}}
    assert resolve_json_path(data, "user.profile.id") == 123
    assert resolve_json_path(data, "user.profile.email") is None


def test_resolve_json_path_list_access() -> None:
    data = {"items": ["first", "second", {"value": 42}]}
    assert resolve_json_path(data, "items[2].value") == 42
    assert resolve_json_path(data, "items[5]") is None
