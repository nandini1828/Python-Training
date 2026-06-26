"""Test suite for dictionary manager."""
import pytest
from app.data_structure_methods.dictionaries import DictionaryManager


class TestDictionaryManager:
    def test_merging_dicts(self):
        result = DictionaryManager.merging_dicts()
        merged = result["merged_unpacking"]
        assert "a" in merged
        assert "d" in merged
    
    def test_nested_dictionaries(self):
        result = DictionaryManager.nested_dictionaries()
        assert result["city"] == "Springfield"
