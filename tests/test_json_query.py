from collection_utils.dict_utils import query_json


def test_query_json_found_key():
    data = {"user": {"profile": {"name": "Alice"}}}
    assert query_json(data, "user.profile.name") == "Alice"


def test_query_json_missing_key_returns_default():
    data = {"user": {"profile": {"name": "Alice"}}}
    assert query_json(data, "user.profile.age", 18) == 18
