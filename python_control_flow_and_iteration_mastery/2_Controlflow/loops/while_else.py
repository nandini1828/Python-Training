"""
while_else.py

Demonstrates Python while-else.
"""


class WhileElseExamples:
    """
    Utility class demonstrating
    while-else statements.
    """

    @staticmethod
    def count(limit: int) -> list[int]:
        """
        Counts using while-else.
        """

        result = []
        number = 1

        while number <= limit:
            result.append(number)
            number += 1

        else:
            result.append("Completed")

        return result

    @staticmethod
    def search_number(
        numbers: list[int],
        target: int
    ) -> str:
        """
        Searches using while-else.
        """

        index = 0

        while index < len(numbers):

            if numbers[index] == target:
                return "Number Found"

            index += 1

        else:
            return "Number Not Found"