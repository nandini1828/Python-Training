from typing import Any, Iterable, List, Set, Tuple


def symmetric_difference(left: Iterable[Any], right: Iterable[Any]) -> Set[Any]:
    return set(left).symmetric_difference(right)


def intersection_summary(left: Iterable[Any], right: Iterable[Any]) -> Dict[str, Any]:
    left_set = set(left)
    right_set = set(right)
    return {
        "intersection": list(left_set & right_set),
        "left_only": list(left_set - right_set),
        "right_only": list(right_set - left_set),
    }


def set_statistics(source: Iterable[Any]) -> Dict[str, int]:
    values = set(source)
    return {"count": len(values), "unique": len(values)}
