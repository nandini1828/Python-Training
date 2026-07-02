"""
pass_statement.py

Demonstrates Python pass statement.
"""


class PassExamples:
    """
    Utility class demonstrating
    the pass statement.
    """

    @staticmethod
    def empty_if(number: int) -> str:
        """
        Demonstrates pass inside
        an if statement.
        """

        if number > 0:
            pass

        return "Execution Completed"

    @staticmethod
    def empty_loop(limit: int) -> str:
        """
        Demonstrates pass inside
        a loop.
        """

        for _ in range(limit):
            pass

        return "Loop Completed"

    @staticmethod
    def skip_even_numbers(numbers: list[int]) -> list[int]:
        """
        Uses pass for even numbers.
        """

        result = []

        for number in numbers:

            if number % 2 == 0:
                pass

            result.append(number)

        return result

    @staticmethod
    def placeholder_function() -> str:
        """
        Demonstrates a placeholder
        function.
        """

        pass

        return "Placeholder Function"