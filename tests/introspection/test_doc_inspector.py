"""Test suite for doc inspector."""
import pytest
from app.introspection import DocInspector


class TestDocInspector:
    def test_get_docstring(self):
        def example_func():
            """Example function."""
            pass
        
        doc = DocInspector.get_docstring(example_func)
        assert "Example function" in doc
