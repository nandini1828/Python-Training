import unittest

from day2.core.json_query_engine import (
    NestedJSONQueryEngine
)


class TestJSONQueryEngine(
    unittest.TestCase
):

    def test_valid_path(self):

        data = {
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
            data,
            "user.profile.name"
        )

        self.assertEqual(
            result,
            "Karthik"
        )

    def test_invalid_path(self):

        data = {
            "user": {}
        }

        engine = (
            NestedJSONQueryEngine()
        )

        result = engine.query(
            data,
            "user.profile.age",
            18
        )

        self.assertEqual(
            result,
            18
        )


if __name__ == "__main__":
    unittest.main()