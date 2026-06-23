"""
Test suite for StringDemo class.
"""

import pytest
from app.primitive_datatypes import StringDemo


class TestStringDemo:
    """Test cases for string demonstrations."""
    
    def test_string_concatenation(self):
        """Test string concatenation methods."""
        result = StringDemo.string_concatenation()
        assert result["plus_operator"] == "Hello Alice"
        assert result["multiplication"] == "==========" 
        assert "Alice" in result["f_string"]
    
    def test_string_indexing_slicing(self):
        """Test string indexing and slicing."""
        result = StringDemo.string_indexing_slicing()
        assert result["first_character"] == "P"
        assert result["last_character"] == "n"
        assert result["slice_first_three"] == "Pyt"
        assert result["reverse"] == "nohtyP"
        assert result["length"] == 6
    
    def test_string_methods(self):
        """Test common string methods."""
        result = StringDemo.string_methods()
        assert result["lower"] == "  hello world  "
        assert result["upper"] == "  HELLO WORLD  "
        assert result["strip"] == "Hello World"
        assert result["find"] > 0
    
    def test_string_splitting_joining(self):
        """Test string split and join operations."""
        result = StringDemo.string_splitting_joining()
        assert len(result["split_by_comma"]) == 4
        assert result["join"] == "apple, banana, cherry"
    
    def test_string_searching(self):
        """Test string searching."""
        result = StringDemo.string_searching()
        assert result["in_operator"] is True
        assert result["not_in"] is True
        assert result["count_occurrences"] == 2
    
    def test_string_formatting(self):
        """Test string formatting."""
        result = StringDemo.string_formatting()
        assert result["decimal_places"] == "3.14"
        assert "%" in result["percentage"]


class TestStringMethods:
    """Test specific string methods."""
    
    def test_immutability(self):
        """Test string immutability."""
        result = StringDemo.string_immutability()
        assert result["original_unchanged"] == "Hello"
        assert result["returns_new_string"] == "Jello"
