from typing import Any


def iterate_list(values: list[Any]) -> list[Any]:
    return [item for item in values]


def enumerate_list(values: list[Any], start: int = 0) -> list[tuple[int, Any]]:
    return list(enumerate(values, start=start))


def find_index(values: list[Any], target: Any) -> list[int]:
    return [index for index, item in enumerate(values) if item == target]


def filter_positive(numbers: list[int]) -> list[int]:
    return [number for number in numbers if number > 0]


def uppercase_items(items: list[str]) -> list[str]:
    return [item.upper() for item in items]


def sum_items(numbers: list[int]) -> int:
    return sum(numbers)


def flatten_list(nested: list[list[Any]]) -> list[Any]:
    return [item for sublist in nested for item in sublist]


def unique_items(values: list[Any]) -> list[Any]:
    return list(dict.fromkeys(values))


def list_summary(values: list[Any]) -> dict[str, Any]:
    return {
        'count': len(values),
        'first': values[0] if values else None,
        'last': values[-1] if values else None,
    }
