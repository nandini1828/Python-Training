from typing import Any, Dict, Iterable, List, Tuple


def tuple_to_list(values: Tuple[Any, ...]) -> List[Any]:
    return list(values)


def tuple_slice(values: Tuple[Any, ...], start: int = 0, end: int = 3) -> Tuple[Any, ...]:
    return values[start:end]


def tuple_statistics(values: Tuple[Any, ...]) -> Dict[str, int]:
    return {
        "length": len(values),
        "unique": len(set(values)),
    }
