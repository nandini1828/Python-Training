from typing import Any


def iterate_dictionary(data: dict[Any, Any]) -> list[tuple[Any, Any]]:
    return list(data.items())


def get_keys(data: dict[Any, Any]) -> list[Any]:
    return list(data.keys())


def get_values(data: dict[Any, Any]) -> list[Any]:
    return list(data.values())


def merge_dictionaries(first: dict[Any, Any], second: dict[Any, Any]) -> dict[Any, Any]:
    result = first.copy()
    result.update(second)
    return result


def dictionary_to_list(data: dict[Any, Any]) -> list[tuple[Any, Any]]:
    return list(data.items())


def invert_dictionary(data: dict[Any, Any]) -> dict[Any, Any]:
    return {value: key for key, value in data.items()}


def count_frequency(items: list[Any]) -> dict[Any, int]:
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq


def find_key(data: dict[Any, Any], key: Any) -> Any:
    return data.get(key)
