from typing import Any


def iterate_set(values: set[Any]) -> list[Any]:
    return list(values)


def union_sets(first: set[Any], second: set[Any]) -> set[Any]:
    return first | second


def intersect_sets(first: set[Any], second: set[Any]) -> set[Any]:
    return first & second


def difference_sets(first: set[Any], second: set[Any]) -> set[Any]:
    return first - second


def is_subset(first: set[Any], second: set[Any]) -> bool:
    return first <= second


def add_item(values: set[Any], item: Any) -> set[Any]:
    result = set(values)
    result.add(item)
    return result


def pop_item(values: set[Any]) -> set[Any]:
    result = set(values)
    if result:
        result.pop()
    return result


def set_from_list(values: list[Any]) -> set[Any]:
    return set(values)
