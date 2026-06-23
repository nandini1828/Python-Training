"""
Float Data Type Demonstrations

This module covers floating-point number operations, precision issues,
and best practices for working with decimal numbers in Python.
"""

from typing import Dict, List, Tuple
import math
from decimal import Decimal, getcontext


class FloatDemo:
    """Demonstrates floating-point data type features and operations."""

    @staticmethod
    def basic_float_operations() -> dict:
        """
        Demonstrate basic arithmetic operations with floats.
        
        Returns:
            dict: Dictionary containing float operation results.
        """
        a, b = 10.5, 3.2
        
        return {
            "addition": a + b,
            "subtraction": a - b,
            "multiplication": a * b,
            "division": a / b,
            "floor_division": a // b,
            "modulo": a % b,
            "exponentiation": a ** 2,
            "negation": -a,
        }

    @staticmethod
    def floating_point_precision() -> dict:
        """
        Demonstrate floating-point precision issues and surprises.
        
        Returns:
            dict: Dictionary showing precision-related behaviors.
        """
        return {
            "simple_addition": 0.1 + 0.2,                    # Not exactly 0.3
            "is_equal_to_point_three": 0.1 + 0.2 == 0.3,    # False!
            "representation": repr(0.1),                     # Shows actual representation
            "string_representation": str(0.1 + 0.2),         # Rounded for display
            "difference_from_point_three": (0.1 + 0.2) - 0.3,
        }

    @staticmethod
    def float_comparisons() -> dict:
        """
        Demonstrate safe comparison methods for floats.
        
        Returns:
            dict: Dictionary with comparison approaches.
        """
        a, b = 0.1 + 0.2, 0.3
        epsilon = 1e-9
        
        return {
            "direct_comparison": a == b,
            "epsilon_comparison": abs(a - b) < epsilon,
            "math_isclose": math.isclose(a, b),
            "math_isclose_with_tolerance": math.isclose(a, b, abs_tol=1e-10),
        }

    @staticmethod
    def float_special_values() -> dict:
        """
        Demonstrate special float values and their properties.
        
        Returns:
            dict: Dictionary with special float values.
        """
        return {
            "positive_infinity": float("inf"),
            "negative_infinity": float("-inf"),
            "not_a_number": float("nan"),
            "is_inf_positive": math.isinf(float("inf")),
            "is_nan": math.isnan(float("nan")),
            "is_finite": math.isfinite(100.0),
            "nan_comparison": float("nan") == float("nan"),  # False!
        }

    @staticmethod
    def float_methods() -> dict:
        """
        Demonstrate built-in float methods.
        
        Returns:
            dict: Dictionary showing float methods and results.
        """
        num = 42.75
        
        return {
            "hex_representation": num.hex(),
            "is_integer": num.is_integer(),
            "is_integer_when_whole": (42.0).is_integer(),
            "as_integer_ratio": num.as_integer_ratio(),
        }

    @staticmethod
    def rounding_and_formatting() -> dict:
        """
        Demonstrate rounding and formatting floats.
        
        Returns:
            dict: Dictionary with rounding and formatting results.
        """
        num = 3.14159265359
        
        return {
            "round_no_args": round(num),
            "round_2_decimals": round(num, 2),
            "format_2_decimals": f"{num:.2f}",
            "format_4_decimals": f"{num:.4f}",
            "format_scientific": f"{num:e}",
            "format_percentage": f"{0.75:.1%}",
        }

    @staticmethod
    def math_operations() -> dict:
        """
        Demonstrate mathematical operations using the math module.
        
        Returns:
            dict: Dictionary with mathematical function results.
        """
        num = 16.0
        
        return {
            "square_root": math.sqrt(num),
            "ceil": math.ceil(3.2),
            "floor": math.floor(3.8),
            "factorial": math.factorial(5),
            "gcd": math.gcd(48, 18),
            "sin": math.sin(math.pi / 2),
            "cos": math.cos(0),
            "tan": math.tan(math.pi / 4),
            "log": math.log(math.e),
            "log10": math.log10(100),
            "exp": math.exp(1),
            "degrees": math.degrees(math.pi),
            "radians": math.radians(180),
        }

    @staticmethod
    def decimal_precision() -> dict:
        """
        Demonstrate the Decimal module for precise decimal arithmetic.
        
        Returns:
            dict: Dictionary with decimal precision results.
        """
        # Set precision for this operation
        getcontext().prec = 28
        
        a = Decimal("0.1")
        b = Decimal("0.2")
        c = Decimal("0.3")
        
        return {
            "decimal_addition": a + b,
            "decimal_equals_point_three": (a + b) == c,
            "decimal_difference": (a + b) - c,
            "from_float_shows_issue": Decimal(0.1),  # Shows float precision issue
            "from_string_precise": Decimal("0.1"),
        }

    @staticmethod
    def float_conversions() -> dict:
        """
        Demonstrate converting between different numeric types.
        
        Returns:
            dict: Dictionary with conversion results.
        """
        return {
            "int_to_float": float(42),
            "string_to_float": float("3.14"),
            "float_to_int": int(3.9),
            "float_to_string": str(3.14),
            "decimal_to_float": float(Decimal("3.14")),
        }

    @staticmethod
    def statistics_and_sequences() -> List[float]:
        """
        Demonstrate working with sequences of floats.
        
        Returns:
            List[float]: Statistical measures of a float sequence.
        """
        numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
        
        return {
            "sum": sum(numbers),
            "mean": sum(numbers) / len(numbers),
            "max": max(numbers),
            "min": min(numbers),
            "count": len(numbers),
        }
