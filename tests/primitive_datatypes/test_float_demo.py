"""
Test suite for FloatDemo class.
"""

import pytest
import math
from app.primitive_datatypes import FloatDemo


class TestFloatDemo:
    """Test cases for float demonstrations."""
    
    def test_basic_operations(self):
        """Test basic float operations."""
        result = FloatDemo.basic_float_operations()
        assert abs(result["addition"] - 13.7) < 0.01
        assert abs(result["subtraction"] - 7.3) < 0.01
        assert abs(result["division"] - 3.281) < 0.01
    
    def test_floating_point_precision(self):
        """Test floating point precision issues."""
        result = FloatDemo.floating_point_precision()
        assert result["is_equal_to_point_three"] is False
        assert abs(result["simple_addition"] - 0.3) < 0.0001
    
    def test_float_comparisons(self):
        """Test safe float comparisons."""
        result = FloatDemo.float_comparisons()
        assert result["direct_comparison"] is False
        assert result["epsilon_comparison"] is True
        assert result["math_isclose"] is True
    
    def test_float_special_values(self):
        """Test special float values."""
        result = FloatDemo.float_special_values()
        assert math.isinf(result["positive_infinity"])
        assert math.isinf(result["negative_infinity"])
        assert math.isnan(result["not_a_number"])
        assert result["nan_comparison"] is False
    
    def test_float_methods(self):
        """Test float methods."""
        result = FloatDemo.float_methods()
        assert result["is_integer"] is False
        assert (42.0).is_integer() is True
    
    def test_rounding_and_formatting(self):
        """Test rounding and formatting."""
        result = FloatDemo.rounding_and_formatting()
        assert result["round_no_args"] == 3
        assert result["round_2_decimals"] == 3.14
    
    def test_math_operations(self):
        """Test mathematical operations."""
        result = FloatDemo.math_operations()
        assert result["square_root"] == 4.0
        assert result["ceil"] == 4
        assert result["floor"] == 3


class TestDecimalPrecision:
    """Test Decimal precision."""
    
    def test_decimal_precision(self):
        """Test Decimal for precise arithmetic."""
        result = FloatDemo.decimal_precision()
        assert result["decimal_equals_point_three"] is True
