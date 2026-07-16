from collections import Counter, defaultdict, deque
from typing import Any, Dict, Iterable, Iterator, List


def get_object_info(obj: Any) -> Dict[str, Any]:
    return {
        "type": type(obj).__name__,
        "id": id(obj),
        "attributes": dir(obj),
        "is_iterable": hasattr(obj, "__iter__") and not isinstance(obj, (str, bytes)),
    }


def count_items(items: Iterable[Any]) -> Dict[Any, int]:
    return dict(Counter(items))


def group_by(items: Iterable[Dict[str, Any]], key: str) -> Dict[Any, List[Dict[str, Any]]]:
    grouped: Dict[Any, List[Dict[str, Any]]] = defaultdict(list)
    for item in items:
        grouped[item.get(key)].append(item)
    return grouped


def recent_transactions(transactions: Iterable[Dict[str, Any]], limit: int = 5) -> List[Dict[str, Any]]:
    recent = deque(maxlen=limit)
    for transaction in transactions:
        recent.appendleft(transaction)
    return list(recent)
