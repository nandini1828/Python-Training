"""
Numeric Type Casting

This module focuses on conversions between numeric types:
integers, floats, and complex numbers.
"""

from typing import Dict, Union, Tuple
import math
from decimal import Decimal


class NumericCasting:
    """Handles numeric type casting and conversions."""

    @staticmethod
    def int_to_float() -> Dict[str, float]:
        """
        Demonstrate converting integers to floats.
        
        Returns:
            Dict[str, float]: Dictionary with conversion results.
        """
        return {
            "simple_int": float(42),
            "negative_int": float(-100),
            "zero": float(0),
            "large_int": float(10 ** 20),
        }

    @staticmethod
    def float_to_int() -> Dict[str, int]:
        """
        Demonstrate converting floats to integers.
        
        Returns:
            Dict[str, int]: Dictionary with conversion results.
        """
        return {
            "simple_float": int(3.14),
            "truncates_decimal": int(9.99),
            "negative_float": int(-3.5),
            "rounding_not_applied": int(3.9),
        }

    @staticmethod
    def rounding_methods() -> Dict[str, Union[int, float]]:
        """
        Demonstrate different rounding approaches.
        
        Returns:
            Dict[str, Union[int, float]]: Dictionary with rounding results.
        """
        value = 3.7
        
        return {
            "int_truncates": int(value),
            "round_standard": round(value),
            "round_to_1_decimal": round(value, 1),
            "math_floor": math.floor(value),
            "math_ceil": math.ceil(value),
            "math_trunc": math.trunc(value),
        }

    @staticmethod
    def complex_numbers() -> Dict[str, complex]:
        """
        Demonstrate complex number creation and conversion.
        
        Returns:
            Dict[str, complex]: Dictionary with complex number results.
        """
        return {
            "simple_complex": complex(3, 4),
            "from_string": complex("3+4j"),
            "real_part": (3+4j).real,
            "imaginary_part": (3+4j).imag,
            "magnitude": abs(3+4j),
            "conjugate": (3+4j).conjugate(),
        }

    @staticmethod
    def decimal_conversions() -> Dict[str, Union[Decimal, float]]:
        """
        Demonstrate Decimal type conversions.
        
        Returns:
            Dict[str, Union[Decimal, float]]: Dictionary with Decimal results.
        """
        return {
            "int_to_decimal": Decimal(42),
            "string_to_decimal": Decimal("3.14159"),
            "float_to_decimal": Decimal(0.1),  # Shows float precision issue
            "decimal_to_float": float(Decimal("3.14159")),
        }

    @staticmethod
    def type_preservation() -> Dict[str, bool]:
        """
        Demonstrate type preservation in operations.
        
        Returns:
            Dict[str, bool]: Dictionary showing type preservation behavior.
        """
        return {
            "int_plus_int_equals_int": isinstance(5 + 3, int),
            "float_plus_float_equals_float": isinstance(5.0 + 3.0, float),
            "int_plus_float_equals_float": isinstance(5 + 3.0, float),
            "int_times_float_equals_float": isinstance(5 * 3.0, float),
        }

    @staticmethod
    def base_conversions() -> Dict[str, Union[str, int]]:
        """
        Demonstrate number base conversions.
        
        Returns:
            Dict[str, Union[str, int]]: Dictionary with base conversion results.
        """
        num = 255
        
        return {
            "decimal": num,
            "to_binary": bin(num),
            "to_octal": oct(num),
            "to_hex": hex(num),
            "from_binary": int("11111111", 2),
            "from_octal": int("377", 8),
            "from_hex": int("FF", 16),
            "from_hex_lowercase": int("ff", 16),
        }

    @staticmethod
    def numeric_coercions() -> Dict[str, Union[int, float]]:
        """
        Demonstrate implicit numeric coercions.
        
        Returns:
            Dict[str, Union[int, float]]: Dictionary with coercion results.
        """
        return {
            "bool_true_to_int": int(True),      # 1
            "bool_false_to_int": int(False),    # 0
            "bool_true_to_float": float(True),  # 1.0
            "int_divided_by_int": 5 / 2,        # 2.5 (float division)
            "int_floor_div_int": 5 // 2,        # 2 (int floor division)
        }

    @staticmethod
    def overflow_and_precision() -> Dict[str, Union[int, float]]:
        """
        Demonstrate integer arbitrary precision and float limitations.
        
        Returns:
            Dict[str, Union[int, float]]: Dictionary with precision results.
        """
        return {
            "very_large_int": 10 ** 100,
            "int_factorial_20": math.factorial(20),
            "float_precision_loss": 0.1 + 0.2,  # Not exactly 0.3
            "int_no_precision_loss": 1000000000000000 + 1,
        }

    @staticmethod
    def special_numeric_values() -> Dict[str, Union[float, bool]]:
        """
        Demonstrate special numeric values.
        
        Returns:
            Dict[str, Union[float, bool]]: Dictionary with special values.
        """
        return {
            "positive_infinity": float("inf"),
            "negative_infinity": float("-inf"),
            "not_a_number": float("nan"),
            "is_inf": math.isinf(float("inf")),
            "is_nan": math.isnan(float("nan")),
            "is_finite": math.isfinite(100.0),
        }
