from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


def unique_ordered(values: Sequence[Any]) -> List[Any]:
    seen = set()
    unique_list: List[Any] = []
    for element in values:
        if element not in seen:
            seen.add(element)
            unique_list.append(element)
    return unique_list


def paginate_list(values: Sequence[Any], page: int = 1, page_size: int = 10) -> List[Any]:
    if page < 1 or page_size < 1:
        return []
    start = (page - 1) * page_size
    end = start + page_size
    return list(values)[start:end]


def list_statistics(values: Sequence[Any]) -> Dict[str, int]:
    return {
        "count": len(values),
        "unique": len(set(values)),
        "pages": ((len(values) - 1) // 10) + 1 if values else 0,
    }
