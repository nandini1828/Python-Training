from collection_utils.dict_utils import query_json


def demo_json_query():
    data = {"user": {"profile": {"name": "Alice"}}}
    return query_json(data, "user.profile.name"), query_json(data, "user.profile.age", 18)
