"""
for_else.py

Demonstrates Python for-else.
"""


class ForElseExamples:
    """
    Utility class demonstrating
    for-else statements.
    """

    @staticmethod
    def search_number(
        numbers: list[int],
        target: int
    ) -> str:
        """
        Searches for a number.
        """

        for number in numbers:

            if number == target:
                return "Number Found"

        else:
            return "Number Not Found"

    @staticmethod
    def search_name(
        names: list[str],
        name: str
    ) -> str:
        """
        Searches for a name.
        """

        for item in names:

            if item == name:
                return "Name Found"

        else:
            return "Name Not Found"