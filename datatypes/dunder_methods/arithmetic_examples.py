"""
Arithmetic Examples

Demonstrates arithmetic dunder methods.
"""

from typing import Dict


class ArithmeticExamples:
    """Examples of arithmetic dunder methods."""
    
    @staticmethod
    def basic_arithmetic() -> Dict[str, object]:
        """
        Demonstrate basic arithmetic operations.
        
        Returns:
            Dict[str, object]: Arithmetic results.
        """
        a, b = 15, 4
        
        return {
            "addition": a + b,
            "subtraction": a - b,
            "multiplication": a * b,
            "true_division": a / b,
            "floor_division": a // b,
            "modulo": a % b,
            "exponentiation": a ** b,
        }
    
    @staticmethod
    def unary_operators() -> Dict[str, object]:
        """
        Demonstrate unary operators.
        
        Returns:
            Dict[str, object]: Unary operator results.
        """
        num = 42
        
        return {
            "positive": +num,
            "negative": -num,
            "absolute": abs(-num),
            "integer_conversion": int(42.7),
            "float_conversion": float(42),
        }
    
    @staticmethod
    def bitwise_operations() -> Dict[str, int]:
        """
        Demonstrate bitwise arithmetic.
        
        Returns:
            Dict[str, int]: Bitwise operation results.
        """
        a, b = 12, 5  # 1100 and 0101 in binary
        
        return {
            "bitwise_and": a & b,
            "bitwise_or": a | b,
            "bitwise_xor": a ^ b,
            "bitwise_not": ~a,
            "left_shift": a << 2,
            "right_shift": a >> 2,
        }
    
    @staticmethod
    def augmented_assignment() -> Dict[str, object]:
        """
        Demonstrate augmented assignment operators.
        
        Returns:
            Dict[str, object]: Augmented assignment results.
        """
        results = {}
        
        # Demonstrate each operator
        x = 10
        x += 5
        results["after_plus_equals"] = x  # 15
        
        x = 10
        x -= 3
        results["after_minus_equals"] = x  # 7
        
        x = 10
        x *= 2
        results["after_times_equals"] = x  # 20
        
        x = 10
        x //= 3
        results["after_floor_div_equals"] = x  # 3
        
        x = 10
        x %= 3
        results["after_mod_equals"] = x  # 1
        
        x = 2
        x **= 8
        results["after_power_equals"] = x  # 256
        
        return results
    
    @staticmethod
    def arithmetic_with_floats() -> Dict[str, float]:
        """
        Demonstrate arithmetic with floating-point numbers.
        
        Returns:
            Dict[str, float]: Float arithmetic results.
        """
        a, b = 10.5, 3.2
        
        return {
            "float_addition": a + b,
            "float_subtraction": a - b,
            "float_multiplication": a * b,
            "float_division": a / b,
            "float_floor_division": a // b,
            "float_modulo": a % b,
        }
    
    @staticmethod
    def type_conversion_in_arithmetic() -> Dict[str, object]:
        """
        Demonstrate type coercion in arithmetic.
        
        Returns:
            Dict[str, object]: Type conversion results.
        """
        return {
            "int_plus_int": 5 + 3,
            "int_plus_float": 5 + 3.2,
            "result_type_mixed": type(5 + 3.2).__name__,
            "bool_plus_int": True + 5,  # bool is int
            "int_plus_bool": 10 + False,  # False is 0
        }
    
    @staticmethod
    def complex_number_arithmetic() -> Dict[str, object]:
        """
        Demonstrate arithmetic with complex numbers.
        
        Returns:
            Dict[str, object]: Complex number results.
        """
        c1 = 3 + 4j
        c2 = 1 + 2j
        
        return {
            "complex_addition": c1 + c2,
            "complex_subtraction": c1 - c2,
            "complex_multiplication": c1 * c2,
            "complex_division": c1 / c2,
            "complex_magnitude": abs(c1),
            "complex_conjugate": c1.conjugate(),
        }
    
    @staticmethod
    def division_examples() -> Dict[str, object]:
        """
        Demonstrate different division operations.
        
        Returns:
            Dict[str, object]: Division results.
        """
        return {
            "true_division_int": 7 / 2,  # 3.5
            "true_division_float": 7.0 / 2.0,  # 3.5
            "floor_division": 7 // 2,  # 3
            "modulo": 7 % 2,  # 1
            "divmod_result": divmod(7, 2),  # (3, 1)
            "negative_division": -7 // 2,  # -4 (floor toward -inf)
        }
