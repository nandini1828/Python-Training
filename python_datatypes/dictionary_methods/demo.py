from typing import Dict

from .dictionary_utils import filter_dictionary, flatten_dictionary, merge_dictionary


def run_dictionary_demo() -> None:
    base: Dict[str, object] = {"id": 12, "name": "Atlas", "metadata": {"region": "us-east-1", "tier": "gold"}}
    override: Dict[str, object] = {"name": "Atlas DB", "active": True}
    merged = merge_dictionary(base, override)
    filtered = filter_dictionary(merged, ["id", "name", "active"])
    flattened = flatten_dictionary(merged)

    print("Merged dictionary:", merged)
    print("Filtered dictionary:", filtered)
    print("Flattened dictionary:", flattened)
