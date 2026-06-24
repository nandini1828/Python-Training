"""
Exercise implementations package
"""

from .queue import SimpleQueue
from .tag_merger import merge_tags
from .json_query import JsonQuery
from .word_counter import WordCounter

__all__ = [
    "SimpleQueue",
    "merge_tags",
    "JsonQuery",
    "WordCounter"
]