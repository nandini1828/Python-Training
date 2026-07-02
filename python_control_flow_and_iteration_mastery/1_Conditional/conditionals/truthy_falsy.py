"""
truthy_falsy.py

Demonstrates Python Truthy and Falsy values.

Topics Covered:
- Truthy values
- Falsy values
- Boolean evaluation
- Real-world examples
"""

from typing import Any


class TruthyFalsyExamples:
    """
    Utility class demonstrating Python
    Truthy and Falsy concepts.
    """

    @staticmethod
    def is_truthy(value: Any) -> bool:
        """
        Returns True if value is truthy.

        Args:
            value: Any Python object

        Returns:
            Boolean result
        """

        return bool(value)

    @staticmethod
    def is_falsy(value: Any) -> bool:
        """
        Returns True if value is falsy.

        Args:
            value: Any Python object

        Returns:
            Boolean result
        """

        return not bool(value)

    @staticmethod
    def check_collection(collection: Any) -> str:
        """
        Checks whether a collection
        is empty or contains elements.

        Args:
            collection: Any iterable

        Returns:
            Status message
        """

        if collection:
            return "Collection Contains Data"

        return "Collection Is Empty"

    @staticmethod
    def check_username(username: str) -> str:
        """
        Checks whether username
        is provided.

        Args:
            username: User input

        Returns:
            Validation message
        """

        if username:
            return "Username Entered"

        return "Username Missing"

    @staticmethod
    def check_optional_value(value: Any) -> str:
        """
        Checks whether an optional
        value exists.

        Args:
            value: Any object

        Returns:
            Status message
        """

        if value:
            return "Value Available"

        return "Value Not Available"

    @staticmethod
    def check_api_response(data: dict) -> str:
        """
        Checks whether API returned data.

        Args:
            data: API response

        Returns:
            Response status
        """

        if data:
            return "Data Received"

        return "No Data Received"

    @staticmethod
    def validate_login(username: str, password: str) -> str:
        """
        Validates login using truthy values.

        Args:
            username: Username
            password: Password

        Returns:
            Login validation message
        """

        if username and password:
            return "Login Request Accepted"

        return "Username or Password Missing"

    @staticmethod
    def check_number(number: int) -> str:
        """
        Demonstrates that zero is falsy.

        Args:
            number: Integer value

        Returns:
            Status message
        """

        if number:
            return "Non-Zero Number"

        return "Zero Is Falsy"

    @staticmethod
    def get_default_name(name: str) -> str:
        """
        Demonstrates the use of Truthy/Falsy
        with the 'or' operator.

        Args:
            name: User name

        Returns:
            Name or default value
        """

        return name or "Guest"

    @staticmethod
    def demonstrate_falsy_values() -> list[Any]:
        """
        Returns common falsy values.

        Returns:
            List of falsy values
        """

        return [
            None,
            False,
            0,
            0.0,
            "",
            [],
            (),
            {},
            set()
        ]