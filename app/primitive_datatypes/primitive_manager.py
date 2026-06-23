"""
Primitive Data Types Manager

This module provides a unified interface for demonstrating
and testing all primitive data types.
"""

from typing import Dict, Any
from .integer_demo import IntegerDemo
from .float_demo import FloatDemo
from .string_demo import StringDemo
from .boolean_demo import BooleanDemo


class PrimitiveManager:
    """Manager class for primitive data type demonstrations."""

    def __init__(self):
        """Initialize the primitive manager with demo classes."""
        self.integer_demo = IntegerDemo()
        self.float_demo = FloatDemo()
        self.string_demo = StringDemo()
        self.boolean_demo = BooleanDemo()

    def get_all_demonstrations(self) -> Dict[str, Dict[str, Any]]:
        """
        Get all demonstrations from all primitive type classes.
        
        Returns:
            Dict[str, Dict[str, Any]]: Nested dictionary with all demonstrations.
        """
        return {
            "integer": self.get_integer_demonstrations(),
            "float": self.get_float_demonstrations(),
            "string": self.get_string_demonstrations(),
            "boolean": self.get_boolean_demonstrations(),
        }

    def get_integer_demonstrations(self) -> Dict[str, Any]:
        """
        Get all integer demonstrations.
        
        Returns:
            Dict[str, Any]: Dictionary with integer demonstrations.
        """
        return {
            "basic_operations": self.integer_demo.basic_operations(),
            "bitwise_operations": self.integer_demo.bitwise_operations(),
            "integer_representations": self.integer_demo.integer_representations(),
            "integer_properties": self.integer_demo.integer_properties(),
            "abs_and_pow": self.integer_demo.abs_and_pow(),
            "integer_methods": self.integer_demo.integer_methods(),
            "integer_comparisons": self.integer_demo.integer_comparisons(),
            "large_integer_arithmetic": self.integer_demo.large_integer_arithmetic(),
        }

    def get_float_demonstrations(self) -> Dict[str, Any]:
        """
        Get all float demonstrations.
        
        Returns:
            Dict[str, Any]: Dictionary with float demonstrations.
        """
        return {
            "basic_operations": self.float_demo.basic_float_operations(),
            "floating_point_precision": self.float_demo.floating_point_precision(),
            "float_comparisons": self.float_demo.float_comparisons(),
            "float_special_values": self.float_demo.float_special_values(),
            "float_methods": self.float_demo.float_methods(),
            "rounding_and_formatting": self.float_demo.rounding_and_formatting(),
            "math_operations": self.float_demo.math_operations(),
            "decimal_precision": self.float_demo.decimal_precision(),
            "float_conversions": self.float_demo.float_conversions(),
            "statistics_and_sequences": self.float_demo.statistics_and_sequences(),
        }

    def get_string_demonstrations(self) -> Dict[str, Any]:
        """
        Get all string demonstrations.
        
        Returns:
            Dict[str, Any]: Dictionary with string demonstrations.
        """
        return {
            "string_creation": self.string_demo.string_creation(),
            "string_concatenation": self.string_demo.string_concatenation(),
            "string_indexing_slicing": self.string_demo.string_indexing_slicing(),
            "string_methods": self.string_demo.string_methods(),
            "string_splitting_joining": self.string_demo.string_splitting_joining(),
            "string_searching": self.string_demo.string_searching(),
            "string_formatting": self.string_demo.string_formatting(),
            "string_regex": self.string_demo.string_regex(),
            "string_immutability": self.string_demo.string_immutability(),
            "string_special_characters": self.string_demo.string_special_characters(),
        }

    def get_boolean_demonstrations(self) -> Dict[str, Any]:
        """
        Get all boolean demonstrations.
        
        Returns:
            Dict[str, Any]: Dictionary with boolean demonstrations.
        """
        return {
            "boolean_basics": self.boolean_demo.boolean_basics(),
            "logical_operators": self.boolean_demo.logical_operators(),
            "comparison_operators": self.boolean_demo.comparison_operators(),
            "truthiness": self.boolean_demo.truthiness(),
            "conditional_expressions": self.boolean_demo.conditional_expressions(),
            "boolean_in_collections": self.boolean_demo.boolean_in_collections(),
            "boolean_with_none": self.boolean_demo.boolean_with_none(),
            "boolean_string_conversion": self.boolean_demo.boolean_string_conversion(),
            "boolean_logic_operations": self.boolean_demo.boolean_logic_operations(),
            "boolean_filtering": self.boolean_demo.boolean_filtering(),
        }

    def print_all_demonstrations(self) -> None:
        """
        Print all demonstrations in a formatted manner.
        """
        all_demos = self.get_all_demonstrations()
        
        for data_type, demonstrations in all_demos.items():
            print(f"\n{'=' * 60}")
            print(f"{data_type.upper()} DEMONSTRATIONS")
            print('=' * 60)
            
            for demo_name, demo_result in demonstrations.items():
                print(f"\n{demo_name.replace('_', ' ').title()}:")
                if isinstance(demo_result, dict):
                    for key, value in demo_result.items():
                        print(f"  {key}: {value}")
                else:
                    print(f"  {demo_result}")

    def run_comparison_test(self) -> Dict[str, bool]:
        """
        Run comparison tests between different primitive types.
        
        Returns:
            Dict[str, bool]: Dictionary with test results.
        """
        return {
            "int_equals_float": 10 == 10.0,
            "int_less_than_float": 5 < 10.0,
            "string_different_from_number": "10" != 10,
            "true_equals_one": True == 1,
            "false_equals_zero": False == 0,
            "none_not_equal_to_false": None != False,
        }
