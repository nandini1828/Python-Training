from .dictionary_methods import (
    safe_get,
    set_default_example,
    merge_dicts
)

from .json_query import query_json

from .vocabulary import word_count

__all__ = [
    "safe_get",
    "set_default_example",
    "merge_dicts",
    "query_json",
    "word_count"
]