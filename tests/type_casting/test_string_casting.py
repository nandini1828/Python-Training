"""Test suite for StringCasting."""
import pytest
from app.type_casting import StringCasting


class TestStringCasting:
    def test_number_to_string(self):
        result = StringCasting.number_to_string()
        assert result["int_to_string"] == "42"
        assert result["float_to_string"] == "3.14159"
    
    def test_string_to_number(self):
        result = StringCasting.string_to_number()
        assert result["string_to_int"] == 42
        assert result["string_to_float"] == 3.14159
    
    def test_boolean_to_string(self):
        result = StringCasting.boolean_to_string()
        assert result["true_to_string"] == "True"
        assert result["false_to_string"] == "False"
    
    def test_list_to_string(self):
        result = StringCasting.list_to_string()
        assert "[1, 2, 3, 4, 5]" in result["str_function"]
        assert "1-2-3-4-5" in result["join_with_custom_sep"] or "-" in result["join_with_custom_sep"]
    
    def test_dict_to_string(self):
        result = StringCasting.dict_to_string()
        assert "name" in result["str_function"]
