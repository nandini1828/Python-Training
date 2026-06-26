"""
Boolean Data Type Demonstrations

This module covers boolean operations, truthiness, logical operators,
and best practices for working with boolean values in Python.
"""

from typing import List, Dict


class BooleanDemo:
    """Demonstrates boolean data type features and operations."""

    @staticmethod
    def boolean_basics() -> dict:
        """
        Demonstrate basic boolean values and operations.
        
        Returns:
            dict: Dictionary with basic boolean operations.
        """
        return {
            "true_value": True,
            "false_value": False,
            "type_of_true": type(True).__name__,
            "type_of_false": type(False).__name__,
            "int_representation_true": int(True),
            "int_representation_false": int(False),
            "bool_of_one": bool(1),
            "bool_of_zero": bool(0),
        }

    @staticmethod
    def logical_operators() -> dict:
        """
        Demonstrate logical operators (and, or, not).
        
        Returns:
            dict: Dictionary with logical operator results.
        """
        a, b, c = True, False, True
        
        return {
            "and_true_true": a and b,           # False
            "and_true_false": a and c,          # True
            "or_true_false": a or b,            # True
            "or_false_false": b or False,       # False
            "not_true": not a,                  # False
            "not_false": not b,                 # True
            "complex_and_or": (a and b) or c,  # True
            "complex_or_and": (a or b) and c,  # True
        }

    @staticmethod
    def short_circuit_evaluation() -> dict:
        """
        Demonstrate short-circuit evaluation in logical operators.
        
        Returns:
            dict: Dictionary showing short-circuit behavior.
        """
        def side_effect():
            """Function with side effect - prints when called."""
            print("Side effect executed!")
            return True
        
        return {
            "and_short_circuit": False and side_effect(),  # side_effect() NOT called
            "or_short_circuit": True or side_effect(),     # side_effect() NOT called
            "and_evaluates_both": True and side_effect(),  # side_effect() IS called
            "or_evaluates_second": False or side_effect(), # side_effect() IS called
        }

    @staticmethod
    def comparison_operators() -> dict:
        """
        Demonstrate comparison operators that return booleans.
        
        Returns:
            dict: Dictionary with comparison results.
        """
        a, b, c = 10, 20, 10
        
        return {
            "equal": a == b,
            "not_equal": a != b,
            "less_than": a < b,
            "greater_than": a > b,
            "less_or_equal": a <= c,
            "greater_or_equal": a >= c,
            "is_same_object": a is c,
            "is_not_same": a is not b,
            "in_list": 10 in [10, 20, 30],
            "not_in_list": 5 not in [10, 20, 30],
        }

    @staticmethod
    def truthiness() -> dict:
        """
        Demonstrate truthiness - values that evaluate to True or False.
        
        Returns:
            dict: Dictionary showing truthiness of various values.
        """
        return {
            "truthy_numbers": bool(1) and bool(100) and bool(-5),
            "falsy_numbers": not bool(0),
            "truthy_string": bool("hello"),
            "falsy_empty_string": not bool(""),
            "truthy_list": bool([1, 2, 3]),
            "falsy_empty_list": not bool([]),
            "truthy_dict": bool({"key": "value"}),
            "falsy_empty_dict": not bool({}),
            "falsy_none": not bool(None),
        }

    @staticmethod
    def conditional_expressions() -> dict:
        """
        Demonstrate conditional expressions and ternary operator.
        
        Returns:
            dict: Dictionary with conditional expression results.
        """
        age = 25
        score = 75
        
        return {
            "ternary_operator": "Adult" if age >= 18 else "Minor",
            "ternary_score": "Pass" if score >= 60 else "Fail",
            "nested_ternary": (
                "Excellent" if score >= 90 else
                "Good" if score >= 80 else
                "Fair" if score >= 70 else
                "Poor"
            ),
            "boolean_and_assignment": ("Yes" if True else "No"),
        }

    @staticmethod
    def boolean_in_collections() -> dict:
        """
        Demonstrate boolean usage in collections.
        
        Returns:
            dict: Dictionary with boolean collection operations.
        """
        values = [True, False, True, True, False]
        
        return {
            "count_true": sum(values),  # True is 1, False is 0
            "count_false": len(values) - sum(values),
            "any_true": any(values),     # True if any element is True
            "all_true": all(values),     # True only if all are True
            "all_true_for_all": all([True, True, True]),
        }

    @staticmethod
    def boolean_with_none() -> dict:
        """
        Demonstrate boolean operations with None values.
        
        Returns:
            dict: Dictionary with None-related boolean operations.
        """
        value = None
        default = "N/A"
        
        return {
            "none_is_falsy": not bool(None),
            "none_comparison": None is None,
            "none_is_not_false": None is not False,
            "or_with_none": value or default,
            "checking_none": value is None,
            "coalesce": value or "default_value",
        }

    @staticmethod
    def boolean_string_conversion() -> dict:
        """
        Demonstrate string representation of booleans.
        
        Returns:
            dict: Dictionary with boolean string conversions.
        """
        return {
            "str_true": str(True),
            "str_false": str(False),
            "repr_true": repr(True),
            "repr_false": repr(False),
            "bool_from_string_nonempty": bool("False"),  # "False" is truthy!
            "bool_from_string_empty": bool(""),
            "direct_bool_true": bool(True),
            "direct_bool_false": bool(False),
        }

    @staticmethod
    def boolean_logic_operations() -> dict:
        """
        Demonstrate advanced boolean logic operations.
        
        Returns:
            dict: Dictionary with boolean logic results.
        """
        # De Morgan's Laws
        a, b = True, False
        
        return {
            "de_morgans_and": (not (a and b)) == (not a or not b),
            "de_morgans_or": (not (a or b)) == (not a and not b),
            "xor_simulation": (a or b) and not (a and b),  # XOR: True if only one is True
            "implication": (not a) or b,  # a implies b = not a or b
        }

    @staticmethod
    def boolean_filtering() -> dict:
        """
        Demonstrate using booleans to filter data.
        
        Returns:
            dict: Dictionary with filtering results.
        """
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        return {
            "filter_even": [n for n in numbers if n % 2 == 0],
            "filter_greater_than_five": [n for n in numbers if n > 5],
            "filter_with_bool_function": list(filter(lambda x: x > 5, numbers)),
        }
