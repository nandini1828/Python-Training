import argparse

from exercises.nested_json_query_engine import (
    NestedJSONQueryEngine
)

def main():

    parser = argparse.ArgumentParser(
        description="JSON Query Tool"
    )

    parser.add_argument(
        "--path",
        required=True,
        help="JSON path"
    )

    args = parser.parse_args()

    sample_data = {
        "user": {
            "profile": {
                "name": "Karthik"
            }
        }
    }

    engine = (
        NestedJSONQueryEngine()
    )

    result = engine.query(
        sample_data,
        args.path
    )

    print(result)


if __name__ == "__main__":
    main()



# To run it
# python cli/json_cli.py \
# --path user.profile.name