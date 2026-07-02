"""Test suite for NumericCasting."""
import pytest
import math
from datatypes.type_casting import NumericCasting


class TestNumericCasting:
    def test_int_to_float(self):
        result = NumericCasting.int_to_float()
        assert result["simple_int"] == 42.0
        assert isinstance(result["simple_int"], float)
    
    def test_float_to_int(self):
        result = NumericCasting.float_to_int()
        assert result["simple_float"] == 3
        assert result["truncates_decimal"] == 9
    
    def test_rounding_methods(self):
        result = NumericCasting.rounding_methods()
        assert result["round_standard"] == 4
        assert result["math_ceil"] == 4
        assert result["math_floor"] == 3
    
    def test_complex_numbers(self):
        result = NumericCasting.complex_numbers()
        assert result["simple_complex"] == 3+4j
        assert result["magnitude"] == 5
    
    def test_type_preservation(self):
        result = NumericCasting.type_preservation()
        assert result["int_plus_int_equals_int"] is True
        assert result["int_plus_float_equals_float"] is True
