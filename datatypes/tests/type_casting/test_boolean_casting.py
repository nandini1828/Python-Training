"""Test suite for BooleanCasting."""
import pytest
from datatypes.type_casting import BooleanCasting


class TestBooleanCasting:
    def test_number_to_boolean(self):
        result = BooleanCasting.number_to_boolean()
        assert result["zero_is_false"] is False
        assert result["positive_is_true"] is True
        assert result["negative_is_true"] is True
    
    def test_string_to_boolean(self):
        result = BooleanCasting.string_to_boolean()
        assert result["empty_string_is_false"] is False
        assert result["nonempty_string_is_true"] is True
        assert result["zero_string_is_true"] is True
    
    def test_collection_to_boolean(self):
        result = BooleanCasting.collection_to_boolean()
        assert result["empty_list_is_false"] is False
        assert result["nonempty_list_is_true"] is True
    
    def test_all_and_any(self):
        result = BooleanCasting.all_and_any()
        assert result["all_truthy"] is True
        assert result["all_mixed"] is False
        assert result["any_truthy"] is True
