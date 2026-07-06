from typing import Any, Iterable, Mapping, Sequence


def square_dict(numbers: Iterable[int]) -> dict[int, int]:
    """Map each number to its square."""
    return {number: number * number for number in numbers}


def dict_from_lists(keys: Sequence[str], values: Sequence[Any]) -> dict[str, Any]:
    """Create a dictionary from matching key and value positions."""
    return {key: value for key, value in zip(keys, values)}


def uppercase_keys(data: Mapping[str, Any]) -> dict[str, Any]:
    """Return a copy with uppercase string keys."""
    return {key.upper(): value for key, value in data.items()}


def value_length_dict(strings: Iterable[str]) -> dict[str, int]:
    """Map each string to its length."""
    return {string: len(string) for string in strings}


def filter_dict(data: Mapping[str, int], min_value: int) -> dict[str, int]:
    """Return items whose value is at least min_value."""
    return {key: value for key, value in data.items() if value >= min_value}


def invert_unique(data: Mapping[str, Any]) -> dict[Any, str]:
    """Invert a dictionary when values are unique and hashable."""
    return {value: key for key, value in data.items()}


def normalize_scores(scores: Mapping[str, int], max_score: int) -> dict[str, float]:
    """Return scores as percentages rounded to two decimal places."""
    if max_score <= 0:
        raise ValueError("max_score must be greater than zero")

    return {
        name: round((score / max_score) * 100, 2)
        for name, score in scores.items()
    }
