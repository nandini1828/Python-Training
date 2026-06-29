"""
Demo Program for Introspection
"""

from introspection.introspection_utils import (
    inspect_object
)


class APIResponse:
    """
    Represents a sample API response.
    """

    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def get_response(self):
        return f"{self.status_code} - {self.message}"


def main():
    """
    Driver Function
    """

    response = APIResponse(
        200,
        "Request Successful"
    )

    import json

    print(json.dumps(inspect_object(response), indent=2))
    print(json.dumps(inspect_object({"server": "localhost", "port": 8080}), indent=2))
    print(json.dumps(inspect_object((10, 20, 30)), indent=2))


if __name__ == "__main__":
    main()