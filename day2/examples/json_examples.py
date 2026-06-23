from day2.core.json_query_engine import (
    NestedJSONQueryEngine
)


def main():

    data = {
        "user": {
            "profile": {
                "name": "Karthik",
                "age": 21
            }
        }
    }

    engine = NestedJSONQueryEngine()

    print(
        engine.query(
            data,
            "user.profile.name"
        )
    )

    print(
        engine.query(
            data,
            "user.profile.city",
            "Not Found"
        )
    )


if __name__ == "__main__":
    main()