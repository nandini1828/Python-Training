from typing import Any, Dict, Iterable, List, Optional, Tuple


def merge_dictionary(*dicts: Dict[str, Any]) -> Dict[str, Any]:
    merged: Dict[str, Any] = {}
    for dictionary in dicts:
        merged.update(dictionary)
    return merged


def filter_dictionary(dictionary: Dict[str, Any], keys: Iterable[str]) -> Dict[str, Any]:
    return {key: dictionary[key] for key in keys if key in dictionary}


def dictionary_statistics(dictionary: Dict[str, Any]) -> Dict[str, int]:
    return {
        "count": len(dictionary),
        "keys": len(set(dictionary.keys())),
        "values": len(list(dictionary.values())),
    }


def flatten_dictionary(dictionary: Dict[str, Any], parent_key: str = "", separator: str = ".") -> Dict[str, Any]:
    flattened: Dict[str, Any] = {}
    for key, value in dictionary.items():
        composed_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened.update(flatten_dictionary(value, parent_key=composed_key, separator=separator))
        else:
            flattened[composed_key] = value
    return flattened
