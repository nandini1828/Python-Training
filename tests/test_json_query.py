from exercises.nested_json_query_engine import (
    NestedJSONQueryEngine
)


def test_valid_path():

    data = {
        "user": {
            "profile": {
                "name": "Karthik"
            }
        }
    }

    engine = NestedJSONQueryEngine()

    assert (
        engine.query(
            data,
            "user.profile.name"
        )
        == "Karthik"
    )


def test_invalid_path():

    data = {
        "user": {}
    }

    engine = NestedJSONQueryEngine()

    assert (
        engine.query(
            data,
            "user.profile.age",
            18
        )
        == 18
    )


def test_list_support():

    data = {
        "users": [
            {
                "name": "Karthik"
            }
        ]
    }

    engine = NestedJSONQueryEngine()

    assert (
        engine.query(
            data,
            "users.0.name"
        )
        == "Karthik"
    )