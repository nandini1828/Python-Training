"""
data_structure_iteration package

Topics covered:
- Lists and slicing
- Safe list modification
- Dictionaries with keys/values/items
- Dictionary key protection with get/defaultdict
- Sets and membership testing
"""

from collections import defaultdict

from .dictionary_iteration import dictionary_iteration
from .dictionary_key_protection import dictionary_key_protection
from .list_iteration import list_iteration_and_slicing
from .list_modification_trap import list_modification_trap
from .set_iteration import set_membership_and_looping
from .set_iteration import run as _set_iteration_run
from .dictionary_iteration import run as _dictionary_iteration_run
from .dictionary_key_protection import run as _dictionary_key_protection_run
from .list_modification_trap import run as _list_modification_trap_run


__all__ = [
    "defaultdict",
    "dictionary_iteration",
    "dictionary_key_protection",
    "list_iteration_and_slicing",
    "list_modification_trap",
    "set_membership_and_looping",
    "run",
]


def run() -> None:
    """Run all data structure iteration examples."""
    products = ["Laptop", "Mouse", "Monitor", "Keyboard"]
    list_iteration_and_slicing(products)
    _list_modification_trap_run()
    _dictionary_iteration_run()
    _dictionary_key_protection_run()
    _set_iteration_run()
