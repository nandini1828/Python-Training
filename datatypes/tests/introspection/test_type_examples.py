"""Test suite for type examples."""
import pytest
from datatypes.introspection import TypeExamples


class TestTypeVsIsinstance:
    def test_type_comparison(self):
        result = TypeExamples.type_comparison()
        assert result["string_equals_string"] is True
        assert result["int_equals_int"] is True
        assert result["list_not_equals_tuple"] is True
    
    def test_type_vs_isinstance(self):
        result = TypeExamples.type_vs_isinstance()
        assert result["type_true_is_bool"] is True
        assert result["isinstance_true_is_int"] is True


class TestCallableCheck:
    def test_callable_type_check(self):
        result = TypeExamples.callable_type_check()
        assert result["function_is_callable"] is True
        assert result["class_is_callable"] is True
        assert result["string_not_callable"] is False
