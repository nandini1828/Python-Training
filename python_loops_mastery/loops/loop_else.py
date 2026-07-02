"""
for-else and while-else examples.
"""


def search_number_with_for_else(numbers: list[int], target: int) -> str:
    """
    Searches for a target using for-else.

    Returns 'Found' if target exists, otherwise 'Not Found'.
    """
    for number in numbers:
        if number == target:
            return "Found"
    else:
        return "Not Found"


def count_with_while_else(limit: int) -> str:
    """
    Demonstrates while-else.
    Returns a message if loop completes without break.
    """
    counter = 1

    while counter <= limit:
        counter += 1
    else:
        return "While loop completed successfully"