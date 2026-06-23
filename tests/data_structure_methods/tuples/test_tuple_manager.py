"""Test suite for tuple manager."""
import pytest
from app.data_structure_methods.tuples import TupleManager


class TestTupleManager:
    def test_tuple_methods(self):
        result = TupleManager.tuple_methods()
        assert result["count"] == 2
        assert result["index"] == 1
    
    def test_immutability(self):
        result = TupleManager.immutability()
        original = result["original_tuple"]
        assert original == (1, 2, 3, 4, 5)
