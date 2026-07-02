"""Test suite for tuple manager."""
import pytest
from datatypes.data_structure_methods.tuples import TupleManager


class TestTupleManager:
    def test_tuple_methods(self):
        result = TupleManager.tuple_methods()
        assert result["count"] == 2
        assert result["index"] == 1
    
    def test_immutability(self):
        result = TupleManager.immutability()
        original = result["original"]
        assert original == (1, 2, 3)
