"""
String Type Casting

This module focuses on converting values to and from strings,
including formatting and parsing operations.
"""

from typing import Any, List, Dict, Union
import json
import ast


class StringCasting:
    """Handles string casting and conversions."""

    @staticmethod
    def number_to_string() -> Dict[str, str]:
        """
        Demonstrate converting numbers to strings.
        
        Returns:
            Dict[str, str]: Dictionary with conversion results.
        """
        return {
            "int_to_string": str(42),
            "float_to_string": str(3.14159),
            "negative_to_string": str(-100),
            "scientific_notation": str(1.23e-4),
        }

    @staticmethod
    def string_to_number() -> Dict[str, Union[int, float]]:
        """
        Demonstrate converting strings to numbers.
        
        Returns:
            Dict[str, Union[int, float]]: Dictionary with conversion results.
        """
        return {
            "string_to_int": int("42"),
            "string_to_float": float("3.14159"),
            "string_with_leading_zeros": int("00042"),
            "string_negative": int("-100"),
            "string_hex": int("0xFF", 16),
            "string_binary": int("101010", 2),
            "string_octal": int("755", 8),
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
            "custom_true": "Yes" if True else "No",
            "custom_false": "Yes" if False else "No",
        }

    @staticmethod
    def string_to_boolean() -> Dict[str, bool]:
        """
        Demonstrate converting strings to booleans.
        
        Returns:
            Dict[str, bool]: Dictionary with conversion results.
        """
        return {
            "nonempty_string_is_truthy": bool("False"),
            "empty_string_is_falsy": bool(""),
            "string_zero_is_truthy": bool("0"),
            "string_true_case_insensitive": "true".lower() == "true",
            "string_false_case_insensitive": "false".lower() == "false",
        }

    @staticmethod
    def list_to_string() -> Dict[str, str]:
        """
        Demonstrate converting lists to strings.
        
        Returns:
            Dict[str, str]: Dictionary with conversion results.
        """
        lst = [1, 2, 3, 4, 5]
        
        return {
            "str_function": str(lst),
            "join_method": ", ".join(map(str, lst)),
            "join_with_custom_sep": "-".join(str(x) for x in lst),
            "json_dumps": json.dumps(lst),
        }

    @staticmethod
    def dict_to_string() -> Dict[str, str]:
        """
        Demonstrate converting dictionaries to strings.
        
        Returns:
            Dict[str, str]: Dictionary with conversion results.
        """
        d = {"name": "Alice", "age": 30, "city": "New York"}
        
        return {
            "str_function": str(d),
            "json_dumps": json.dumps(d),
            "json_with_indent": json.dumps(d, indent=2),
        }

    @staticmethod
    def string_to_list() -> Dict[str, list]:
        """
        Demonstrate converting strings to lists.
        
        Returns:
            Dict[str, list]: Dictionary with conversion results.
        """
        text = "Hello World"
        csv = "apple,banana,cherry"
        
        return {
            "string_to_char_list": list(text),
            "split_by_space": text.split(),
            "split_by_comma": csv.split(","),
            "json_string_to_list": json.loads('["a", "b", "c"]'),
        }

    @staticmethod
    def string_to_dict() -> Dict[str, dict]:
        """
        Demonstrate converting strings to dictionaries.
        
        Returns:
            Dict[str, dict]: Dictionary with conversion results.
        """
        json_string = '{"name": "Alice", "age": 30}'
        dict_string = "{'name': 'Bob', 'age': 25}"
        
        return {
            "json_loads": json.loads(json_string),
            "ast_literal_eval": ast.literal_eval(dict_string),
        }

    @staticmethod
    def string_parsing() -> Dict[str, Any]:
        """
        Demonstrate parsing complex string formats.
        
        Returns:
            Dict[str, Any]: Dictionary with parsing results.
        """
        csv_line = "Alice,30,Engineer"
        date_string = "2024-06-23"
        
        return {
            "csv_split": csv_line.split(","),
            "csv_with_dict": {
                "name": csv_line.split(",")[0],
                "age": int(csv_line.split(",")[1]),
                "job": csv_line.split(",")[2]
            },
            "date_parse": date_string.split("-"),
        }

    @staticmethod
    def case_conversions() -> Dict[str, str]:
        """
        Demonstrate string case conversions.
        
        Returns:
            Dict[str, str]: Dictionary with case conversion results.
        """
        text = "Hello World"
        
        return {
            "lower": text.lower(),
            "upper": text.upper(),
            "title": text.title(),
            "capitalize": text.capitalize(),
            "swapcase": text.swapcase(),
        }

    @staticmethod
    def string_encoding_decoding() -> Dict[str, Any]:
        """
        Demonstrate string encoding and decoding.
        
        Returns:
            Dict[str, Any]: Dictionary with encoding/decoding results.
        """
        text = "Hello, 世界!"
        
        return {
            "encode_utf8": text.encode("utf-8"),
            "encode_ascii_safe": "Hello".encode("ascii"),
            "decode_utf8": b"Hello".decode("utf-8"),
            "encode_to_bytes": text.encode(),
        }
