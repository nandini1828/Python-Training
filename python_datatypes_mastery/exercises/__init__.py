"""
Exercises package with small practice components.
"""

from .queue import SimpleQueue
from .tag_merger import merge_tags
from .json_query import query_json
from .word_counter import word_count

__all__ = ["SimpleQueue", "merge_tags", "query_json", "word_count"]
