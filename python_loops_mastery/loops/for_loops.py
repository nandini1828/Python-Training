"""
for loop examples.
"""


def iterate_list(items: list[str]) -> list[str]:
    """
    Iterates over a list and returns visited items.
    """
    visited_items = []

    for item in items:
        visited_items.append(item)

    return visited_items


def iterate_string(text: str) -> list[str]:
    """
    Iterates over a string and returns each character.
    """
    characters = []

    for character in text:
        characters.append(character)

    return characters


def iterate_range(start: int, stop: int) -> list[int]:
    """
    Iterates over a range and returns numbers.
    """
    numbers = []

    for number in range(start, stop):
        numbers.append(number)

    return numbers