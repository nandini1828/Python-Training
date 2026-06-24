"""
Collections utilities package (renamed to avoid stdlib shadowing).
"""

from .list_utils import demo_list_methods
from .dict_utils import demo_dict_methods
from .set_utils import demo_set_methods
from .tuple_utils import demo_tuple_methods

__all__ = [
    "demo_list_methods",
    "demo_dict_methods",
    "demo_set_methods",
    "demo_tuple_methods",
]
