"""
Test suite for IntegerDemo class.
"""

import pytest
from app.primitive_datatypes import IntegerDemo


class TestIntegerDemo:
    """Test cases for integer demonstrations."""
    
    def test_basic_operations(self):
        """Test basic integer arithmetic operations."""
        result = IntegerDemo.basic_operations()
        assert result["addition"] == 13
        assert result["subtraction"] == 7
        assert result["multiplication"] == 30
        assert result["floor_division"] == 3
        assert result["modulo"] == 1
        assert result["exponentiation"] == 1000
    
    def test_bitwise_operations(self):
        """Test bitwise operations."""
        result = IntegerDemo.bitwise_operations()
        assert result["bitwise_and"] == 4
        assert result["bitwise_or"] == 15
        assert result["bitwise_xor"] == 11
        assert result["left_shift"] == 48
        assert result["right_shift"] == 3
    
    def test_integer_representations(self):
        """Test different number representations."""
        result = IntegerDemo.integer_representations()
        assert result["binary"] == "0b11111111"
        assert result["octal"] == "0o377"
        assert result["hexadecimal"] == "0xff"
        assert result["from_binary"] == 255
    
    def test_abs_and_pow(self):
        """Test abs and power functions."""
        result = IntegerDemo.abs_and_pow()
        assert result["abs_positive"] == 10
        assert result["abs_negative"] == 10
        assert result["pow_basic"] == 256
        assert result["divmod"] == (3, 2)
    
    def test_integer_comparisons(self):
        """Test integer comparison operators."""
        result = IntegerDemo.integer_comparisons()
        assert result["equals"] is False
        assert result["not_equals"] is True
        assert result["less_than"] is True
        assert result["greater_than"] is False
    
    def test_large_integer_arithmetic(self):
        """Test large integer handling."""
        result = IntegerDemo.large_integer_arithmetic()
        assert result["factorial_20"] == 2432902008176640000
        assert isinstance(result["very_large_power"], int)


class TestIntegerMethods:
    """Test integer specific methods."""
    
    def test_integer_methods(self):
        """Test integer methods."""
        result = IntegerDemo.integer_methods()
        assert result["bit_length"] == 6
