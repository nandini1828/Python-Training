"""
Inspectors package collects runtime inspection helpers.
"""

from .method_inspector import get_methods_and_docs
from .documentation_inspector import get_doc_via_dunder, get_doc_via_inspect, get_doc_via_help

__all__ = ["get_methods_and_docs", "get_doc_via_dunder", "get_doc_via_inspect", "get_doc_via_help"]
