"""
Boolean Type Casting

This module focuses on converting values to boolean
and understanding truthiness rules.
"""

from typing import Dict, List, Any


class BooleanCasting:
    """Handles boolean type casting and conversions."""

    @staticmethod
    def number_to_boolean() -> Dict[str, bool]:
        """
        Demonstrate converting numbers to booleans.
        
        Returns:
            Dict[str, bool]: Dictionary with conversion results.
        """
        return {
            "zero_is_false": bool(0),
            "zero_float_is_false": bool(0.0),
            "positive_is_true": bool(42),
            "negative_is_true": bool(-1),
            "small_float_is_true": bool(0.0001),
        }

    @staticmethod
    def string_to_boolean() -> Dict[str, bool]:
        """
        Demonstrate converting strings to booleans.
        
        Returns:
            Dict[str, bool]: Dictionary with conversion results.
        """
        return {
            "empty_string_is_false": bool(""),
            "nonempty_string_is_true": bool("hello"),
            "zero_string_is_true": bool("0"),  # "0" is a nonempty string!
            "false_string_is_true": bool("False"),  # "False" is a nonempty string!
            "whitespace_is_true": bool(" "),
        }

    @staticmethod
    def collection_to_boolean() -> Dict[str, bool]:
        """
        Demonstrate converting collections to booleans.
        
        Returns:
            Dict[str, bool]: Dictionary with conversion results.
        """
        return {
            "empty_list_is_false": bool([]),
            "nonempty_list_is_true": bool([1, 2, 3]),
            "empty_dict_is_false": bool({}),
            "nonempty_dict_is_true": bool({"key": "value"}),
            "empty_tuple_is_false": bool(()),
            "nonempty_tuple_is_true": bool((1,)),
            "empty_set_is_false": bool(set()),
            "nonempty_set_is_true": bool({1, 2, 3}),
        }

    @staticmethod
    def none_to_boolean() -> Dict[str, bool]:
        """
        Demonstrate converting None to boolean.
        
        Returns:
            Dict[str, bool]: Dictionary with conversion results.
        """
        return {
            "none_is_false": bool(None),
            "none_is_falsy": not bool(None),
        }

    @staticmethod
    def boolean_to_string() -> Dict[str, str]:
        """
        Demonstrate converting booleans to strings.
        
        Returns:
            Dict[str, str]: Dictionary with conversion results.
        """
        return {
            "true_to_string": str(True),
            "false_to_string": str(False),
            "true_repr": repr(True),
            "false_repr": repr(False),
        }

    @staticmethod
    def boolean_to_number() -> Dict[str, int]:
        """
        Demonstrate converting booleans to numbers.
        
        Returns:
            Dict[str, int]: Dictionary with conversion results.
        """
        return {
            "true_to_int": int(True),      # 1
            "false_to_int": int(False),    # 0
            "true_to_float": float(True),  # 1.0
            "false_to_float": float(False),  # 0.0
        }

    @staticmethod
    def truthiness_examples() -> Dict[str, bool]:
        """
        Demonstrate Python's truthiness rules.
        
        Returns:
            Dict[str, bool]: Dictionary with truthiness examples.
        """
        return {
            "falsy_values": {
                "none": not None,
                "zero_int": not 0,
                "zero_float": not 0.0,
                "empty_string": not "",
                "empty_list": not [],
                "empty_dict": not {},
                "empty_tuple": not (),
                "empty_set": not set(),
            },
            "truthy_values": {
                "any_int": bool(1) or bool(-5),
                "any_float": bool(3.14),
                "any_string": bool("0") or bool("False"),
                "any_list": bool([None]) or bool([0]),
                "any_dict": bool({None: None}),
                "true_literal": bool(True),
            }
        }

    @staticmethod
    def logical_operators_with_types() -> Dict[str, Any]:
        """
        Demonstrate logical operators with different types.
        
        Returns:
            Dict[str, Any]: Dictionary with operator results.
        """
        return {
            "and_with_falsy": 0 and 100,        # 0 (first falsy)
            "and_with_truthy": 1 and 2,         # 2 (evaluates to last)
            "or_with_falsy": 0 or 100,          # 100 (evaluates to first truthy)
            "or_with_all_falsy": 0 or "" or None,  # None (last value)
            "not_with_int": not 5,              # False
            "not_with_zero": not 0,             # True
        }

    @staticmethod
    def conditional_assignment() -> Dict[str, Any]:
        """
        Demonstrate using boolean conversion for conditional assignments.
        
        Returns:
            Dict[str, Any]: Dictionary with assignment results.
        """
        value = None
        name = ""
        age = 0
        
        return {
            "or_coalescing_none": value or "default",
            "or_coalescing_empty_string": name or "Unknown",
            "or_coalescing_zero": age or 18,
            "ternary_operator": "adult" if age >= 18 else "minor",
            "walrus_operator": (x := 10) if True else 5,  # x = 10
        }

    @staticmethod
    def boolean_filtering() -> Dict[str, list]:
        """
        Demonstrate filtering using boolean conversion.
        
        Returns:
            Dict[str, list]: Dictionary with filtering results.
        """
        data = [0, 1, "", "hello", [], [1, 2], None, False, True]
        
        return {
            "filter_truthy": list(filter(bool, data)),
            "list_comp_truthy": [x for x in data if x],
            "list_comp_falsy": [x for x in data if not x],
        }

    @staticmethod
    def all_and_any() -> Dict[str, bool]:
        """
        Demonstrate all() and any() functions.
        
        Returns:
            Dict[str, bool]: Dictionary with all/any results.
        """
        all_true = [1, 2, 3, 4, 5]
        some_true = [1, 0, 3, 4, 5]
        all_false = [0, "", None, False]
        
        return {
            "all_truthy": all(all_true),
            "all_mixed": all(some_true),
            "all_falsy": all(all_false),
            "any_truthy": any(all_true),
            "any_mixed": any(some_true),
            "any_falsy": any(all_false),
            "empty_list_all": all([]),  # True!
            "empty_list_any": any([]),  # False!
        }
