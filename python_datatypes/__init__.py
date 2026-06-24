"""Python Datatypes learning package.

This package exposes utilities for introspection, JSON querying,
collection helpers, composition examples, and dunder method patterns.
"""

from .composition import Address, Customer, Order, OrderHistory, run_composition_demo
from .dictionary_methods import filter_dictionary, flatten_dictionary, merge_dictionary, dictionary_statistics
from .dunder_methods import ImmutableMatrix, NamingContext, run_dunder_demo
from .introspection import extract_documentation, explore_methods, introspect_object
from .json_query import resolve_json_path
from .list_methods import list_statistics, paginate_list, unique_ordered
from .logging_config import configure_logging
from .main import main
from .set_methods import intersection_summary, set_statistics, symmetric_difference
from .tuple_methods import tuple_slice, tuple_statistics, tuple_to_list

__all__ = [
    "configure_logging",
    "main",
    "resolve_json_path",
    "introspect_object",
    "extract_documentation",
    "explore_methods",
    "merge_dictionary",
    "filter_dictionary",
    "flatten_dictionary",
    "dictionary_statistics",
    "paginate_list",
    "unique_ordered",
    "list_statistics",
    "intersection_summary",
    "symmetric_difference",
    "set_statistics",
    "tuple_to_list",
    "tuple_slice",
    "tuple_statistics",
    "Address",
    "Customer",
    "Order",
    "OrderHistory",
    "ImmutableMatrix",
    "NamingContext",
    "run_composition_demo",
    "run_dunder_demo",
]
