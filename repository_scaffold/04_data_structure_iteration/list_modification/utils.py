from typing import Any


def append_item(values: list[Any], item: Any) -> list[Any]:
    result = values.copy()
    result.append(item)
    return result


def remove_item(values: list[Any], item: Any) -> list[Any]:
    result = values.copy()
    if item in result:
        result.remove(item)
    return result


def insert_item(values: list[Any], index: int, item: Any) -> list[Any]:
    result = values.copy()
    result.insert(index, item)
    return result


def pop_item(values: list[Any]) -> list[Any]:
    result = values.copy()
    if result:
        result.pop()
    return result


def extend_list(values: list[Any], items: list[Any]) -> list[Any]:
    result = values.copy()
    result.extend(items)
    return result


def replace_item(values: list[Any], old: Any, new: Any) -> list[Any]:
    return [new if item == old else item for item in values]


def clear_list(values: list[Any]) -> list[Any]:
    return []


def sorted_copy(values: list[int]) -> list[int]:
    return sorted(values)


def unique_list(values: list[Any]) -> list[Any]:
    return list(dict.fromkeys(values))
