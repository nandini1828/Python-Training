"""
Test suite for BooleanDemo class.
"""

import pytest
from datatypes.primitive_datatypes import BooleanDemo


class TestBooleanDemo:
    """Test cases for boolean demonstrations."""
    
    def test_boolean_basics(self):
        """Test basic boolean values."""
        result = BooleanDemo.boolean_basics()
        assert result["true_value"] is True
        assert result["false_value"] is False
        assert result["int_representation_true"] == 1
        assert result["int_representation_false"] == 0
    
    def test_logical_operators(self):
        """Test logical operators."""
        result = BooleanDemo.logical_operators()
        assert result["and_true_true"] is False
        assert result["and_true_false"] is True
        assert result["or_true_false"] is True
        assert result["not_true"] is False
    
    def test_comparison_operators(self):
        """Test comparison operators."""
        result = BooleanDemo.comparison_operators()
        assert result["equal"] is False
        assert result["not_equal"] is True
        assert result["less_than"] is True
        assert result["greater_than"] is False
    
    def test_truthiness(self):
        """Test truthiness rules."""
        result = BooleanDemo.truthiness()
        assert result["falsy_numbers"] is True
        assert result["truthy_string"] is True
        assert result["falsy_empty_string"] is True
        assert result["falsy_none"] is True
    
    def test_conditional_expressions(self):
        """Test ternary operator."""
        result = BooleanDemo.conditional_expressions()
        assert result["ternary_operator"] == "Adult"
        assert result["ternary_score"] == "Pass"
    
    def test_boolean_with_none(self):
        """Test boolean operations with None."""
        result = BooleanDemo.boolean_with_none()
        assert result["none_is_falsy"] is True
        assert result["none_comparison"] is True
        assert result["none_is_not_false"] is True
