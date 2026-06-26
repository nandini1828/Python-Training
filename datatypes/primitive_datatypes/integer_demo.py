"""
Integer Data Type Demonstrations

This module covers integer operations, properties, and best practices.
Integers in Python have arbitrary precision and support various operations.
"""

from typing import List, Tuple
import sys


class IntegerDemo:
    """Demonstrates integer data type features and operations."""

    @staticmethod
    def basic_operations() -> dict:
        """
        Demonstrate basic arithmetic operations with integers.
        
        Returns:
            dict: Dictionary containing basic operation results.
        """
        a, b = 10, 3
        
        return {
            "addition": a + b,
            "subtraction": a - b,
            "multiplication": a * b,
            "floor_division": a // b,
            "modulo": a % b,
            "exponentiation": a ** b,
            "negation": -a,
        }

    @staticmethod
    def bitwise_operations() -> dict:
        """
        Demonstrate bitwise operations on integers.
        
        Returns:
            dict: Dictionary containing bitwise operation results.
        """
        x, y = 12, 7  # 12 = 1100, 7 = 0111 in binary
        
        return {
            "bitwise_and": x & y,        # 0100 = 4
            "bitwise_or": x | y,         # 1111 = 15
            "bitwise_xor": x ^ y,        # 1011 = 11
            "bitwise_not": ~x,           # -(x+1) = -13
            "left_shift": x << 2,        # 48 (shift left by 2)
            "right_shift": x >> 2,       # 3 (shift right by 2)
        }

    @staticmethod
    def integer_representations() -> dict:
        """
        Demonstrate different representations of integers.
        
        Returns:
            dict: Dictionary with different number base representations.
        """
        num = 255
        
        return {
            "decimal": num,
            "binary": bin(num),          # '0b11111111'
            "octal": oct(num),           # '0o377'
            "hexadecimal": hex(num),     # '0xff'
            "from_binary": int("11111111", 2),
            "from_octal": int("377", 8),
            "from_hex": int("ff", 16),
        }

    @staticmethod
    def integer_properties() -> dict:
        """
        Demonstrate integer properties and size information.
        
        Returns:
            dict: Dictionary containing integer properties.
        """
        large_num = 10 ** 100
        
        return {
            "size_of_small_int": sys.getsizeof(42),
            "size_of_large_int": sys.getsizeof(large_num),
            "is_instance_of_int": isinstance(42, int),
            "is_instance_of_float": isinstance(42, float),
            "type_of_integer": type(42).__name__,
        }

    @staticmethod
    def abs_and_pow() -> dict:
        """
        Demonstrate absolute value and power functions.
        
        Returns:
            dict: Dictionary with results of abs() and pow() functions.
        """
        return {
            "abs_positive": abs(10),
            "abs_negative": abs(-10),
            "pow_basic": pow(2, 8),
            "pow_with_modulo": pow(2, 8, 3),  # (2**8) % 3 = 1
            "divmod": divmod(17, 5),          # (3, 2)
        }

    @staticmethod
    def integer_methods() -> dict:
        """
        Demonstrate built-in integer methods.
        
        Returns:
            dict: Dictionary showing integer methods and their results.
        """
        num = 42
        
        return {
            "bit_length": num.bit_length(),           # 6 (needs 6 bits)
            "to_bytes": num.to_bytes(2, byteorder='big'),
            "from_bytes": int.from_bytes(b'\x00\x2a', byteorder='big'),
        }

    @staticmethod
    def integer_comparisons() -> dict:
        """
        Demonstrate integer comparison operations.
        
        Returns:
            dict: Dictionary with comparison results.
        """
        a, b = 10, 20
        
        return {
            "equals": a == b,
            "not_equals": a != b,
            "less_than": a < b,
            "greater_than": a > b,
            "less_or_equal": a <= b,
            "greater_or_equal": a >= b,
        }

    @staticmethod
    def large_integer_arithmetic() -> dict:
        """
        Demonstrate Python's ability to handle arbitrarily large integers.
        
        Returns:
            dict: Dictionary with large integer results.
        """
        factorial_20 = 1
        for i in range(1, 21):
            factorial_20 *= i
        
        return {
            "factorial_20": factorial_20,
            "very_large_power": 2 ** 1024,
            "fibonacci_100": IntegerDemo._fibonacci(100),
        }

    @staticmethod
    def _fibonacci(n: int) -> int:
        """
        Calculate the nth Fibonacci number.
        
        Args:
            n: The position in Fibonacci sequence.
            
        Returns:
            int: The nth Fibonacci number.
        """
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
