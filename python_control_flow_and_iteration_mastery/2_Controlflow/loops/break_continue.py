"""
break_continue.py

Demonstrates Python break and continue statements.
"""


class BreakContinueExamples:
    """
    Utility class demonstrating
    break and continue statements.
    """

    @staticmethod
    def break_example(numbers: list[int], target: int) -> str:
        """
        Stops searching once the
        target number is found.
        """

        for number in numbers:

            if number == target:
                return f"{target} Found"

        return f"{target} Not Found"

    @staticmethod
    def stop_at_five() -> list[int]:
        """
        Demonstrates break statement.
        """

        result = []

        for number in range(1, 11):

            if number == 5:
                break

            result.append(number)

        return result

    @staticmethod
    def continue_example(numbers: list[int]) -> list[int]:
        """
        Skips even numbers.
        """

        result = []

        for number in numbers:

            if number % 2 == 0:
                continue

            result.append(number)

        return result

    @staticmethod
    def skip_empty_strings(words: list[str]) -> list[str]:
        """
        Skips empty strings.
        """

        result = []

        for word in words:

            if word == "":
                continue

            result.append(word)

        return result