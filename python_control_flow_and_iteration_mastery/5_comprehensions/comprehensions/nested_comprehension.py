"""
nested_comprehension.py

Demonstrates Nested Comprehensions.
"""


class NestedComprehensionExamples:
    """Utility class demonstrating nested comprehensions."""

    @staticmethod
    def flatten_matrix(
        matrix: list[list[int]]
    ) -> list[int]:
        """Flattens nested list."""

        return [
            number
            for row in matrix
            for number in row
        ]

    @staticmethod
    def create_matrix(rows: int, columns: int) -> list[list[int]]:
        """Creates a matrix."""

        return [
            [
                0
                for _ in range(columns)
            ]
            for _ in range(rows)
        ]

    @staticmethod
    def multiplication_table(size: int) -> list[list[int]]:
        """Creates multiplication table."""

        return [
            [
                row * column
                for column in range(1, size + 1)
            ]
            for row in range(1, size + 1)
        ]