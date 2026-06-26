"""Test suite for data structure methods."""
import pytest
from app.data_structure_methods.lists import ListManager
from app.data_structure_methods.tuples import TupleManager
from app.data_structure_methods.sets import SetManager
from app.data_structure_methods.dictionaries import DictionaryManager


class TestListManager:
    def test_basic_operations(self):
        result = ListManager.basic_operations()
        assert result["length"] == 5
        assert result["first_element"] == 1
        assert result["last_element"] == 5


class TestTupleManager:
    def test_basic_operations(self):
        result = TupleManager.basic_operations()
        assert result["length"] == 5
        assert result["first_element"] == 1


class TestSetManager:
    def test_basic_operations(self):
        result = SetManager.basic_operations()
        assert result["length"] == 5
        assert 3 in result["set"]
    
    def test_set_operations(self):
        result = SetManager.set_operations()
        assert 3 in result["union"]
        assert 4 in result["intersection"]


class TestDictionaryManager:
    def test_basic_operations(self):
        result = DictionaryManager.basic_operations()
        assert result["length"] == 3
        assert result["get_a"] == 1
    
    def test_dictionary_comprehension(self):
        result = DictionaryManager.dictionary_comprehension()
        assert result["squares"][4] == 16
        assert result["filtered"][4] == 16
