"""Test suite for introspection modules."""
import pytest
from datatypes.introspection import DirectoryExamples, InstanceOfExamples, TypeExamples


class TestDirectoryExamples:
    def test_dir_of_string(self):
        result = DirectoryExamples.dir_of_string()
        assert isinstance(result, list)
        assert "upper" in result
        assert "lower" in result
    
    def test_dir_filtering(self):
        result = DirectoryExamples.dir_filtering()
        assert result["all_attributes_count"] > 0
        assert len(result["public_methods"]) > 0


class TestInstanceOfExamples:
    def test_basic_isinstance(self):
        result = InstanceOfExamples.basic_isinstance()
        assert result["string_is_str"] is True
        assert result["number_is_int"] is True
        assert result["true_is_int"] is True
    
    def test_isinstance_inheritance(self):
        result = InstanceOfExamples.isinstance_inheritance()
        assert result["dog_is_animal"] is True
        assert result["dog_is_cat"] is False


class TestTypeExamples:
    def test_basic_type_checking(self):
        result = TypeExamples.basic_type_checking()
        assert result["string_type"] == str
        assert result["int_type"] == int
        assert result["list_type"] == list
    
    def test_type_names(self):
        result = TypeExamples.type_names()
        assert result["string_type"] == "str"
        assert result["int_type"] == "int"
        assert result["bool_type"] == "bool"
