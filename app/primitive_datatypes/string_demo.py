"""
String Data Type Demonstrations

This module covers string operations, methods, formatting,
and best practices for working with text in Python.
"""

from typing import List, Dict
import re


class StringDemo:
    """Demonstrates string data type features and operations."""

    @staticmethod
    def string_creation() -> dict:
        """
        Demonstrate different ways to create strings.
        
        Returns:
            dict: Dictionary with various string creation methods.
        """
        return {
            "single_quotes": 'Hello',
            "double_quotes": "World",
            "triple_single_quotes": '''Multi-line
            string using
            triple quotes''',
            "triple_double_quotes": """Another
            multi-line
            string""",
            "raw_string": r"C:\path\to\file",
            "empty_string": "",
        }

    @staticmethod
    def string_concatenation() -> dict:
        """
        Demonstrate string concatenation methods.
        
        Returns:
            dict: Dictionary with concatenation results.
        """
        name = "Alice"
        age = 30
        
        return {
            "plus_operator": "Hello " + name,
            "multiplication": "=" * 10,
            "f_string": f"Name: {name}, Age: {age}",
            "format_method": "Name: {}, Age: {}".format(name, age),
            "format_named": "Name: {n}, Age: {a}".format(n=name, a=age),
            "join_method": " ".join(["Hello", "World"]),
            "percent_formatting": "Name: %s, Age: %d" % (name, age),
        }

    @staticmethod
    def string_indexing_slicing() -> dict:
        """
        Demonstrate string indexing and slicing operations.
        
        Returns:
            dict: Dictionary with indexing and slicing results.
        """
        text = "Python"
        
        return {
            "first_character": text[0],
            "last_character": text[-1],
            "second_character": text[1],
            "slice_first_three": text[:3],
            "slice_last_two": text[-2:],
            "slice_middle": text[1:4],
            "slice_with_step": text[::2],
            "reverse": text[::-1],
            "length": len(text),
        }

    @staticmethod
    def string_methods() -> dict:
        """
        Demonstrate commonly used string methods.
        
        Returns:
            dict: Dictionary with string method results.
        """
        text = "  Hello World  "
        
        return {
            "strip": text.strip(),
            "lstrip": text.lstrip(),
            "rstrip": text.rstrip(),
            "lower": text.lower(),
            "upper": text.upper(),
            "capitalize": "hello world".capitalize(),
            "title": "hello world".title(),
            "swapcase": "Hello World".swapcase(),
            "replace": text.replace("World", "Python"),
            "find": text.find("World"),
            "count": "mississippi".count("i"),
            "startswith": text.startswith("  "),
            "endswith": text.endswith("  "),
            "isdigit": "12345".isdigit(),
            "isalpha": "hello".isalpha(),
            "isalnum": "hello123".isalnum(),
            "isspace": "   ".isspace(),
        }

    @staticmethod
    def string_splitting_joining() -> dict:
        """
        Demonstrate string splitting and joining operations.
        
        Returns:
            dict: Dictionary with split/join results.
        """
        csv_data = "apple,banana,cherry,date"
        words = "The quick brown fox"
        
        return {
            "split_by_comma": csv_data.split(","),
            "split_default": words.split(),
            "split_max_splits": csv_data.split(",", 2),
            "splitlines": "line1\nline2\nline3".splitlines(),
            "join": ", ".join(["apple", "banana", "cherry"]),
            "join_range": "-".join(str(i) for i in range(1, 4)),
        }

    @staticmethod
    def string_searching() -> dict:
        """
        Demonstrate string searching operations.
        
        Returns:
            dict: Dictionary with search results.
        """
        text = "The quick brown fox jumps over the lazy dog"
        
        return {
            "in_operator": "quick" in text,
            "not_in": "cat" not in text,
            "find_position": text.find("quick"),
            "find_not_found": text.find("cat"),
            "index": text.index("quick"),
            "count_occurrences": text.count("the"),
            "startswith": text.startswith("The"),
            "endswith": text.endswith("dog"),
        }

    @staticmethod
    def string_formatting() -> dict:
        """
        Demonstrate advanced string formatting.
        
        Returns:
            dict: Dictionary with formatting examples.
        """
        pi = 3.14159265359
        money = 1234.567
        
        return {
            "decimal_places": f"{pi:.2f}",
            "scientific_notation": f"{pi:e}",
            "percentage": f"{0.85:.1%}",
            "comma_separator": f"{1000000:,}",
            "padding": f"{42:05d}",
            "alignment_left": f"{'hello':<10}",
            "alignment_right": f"{'hello':>10}",
            "alignment_center": f"{'hello':^10}",
            "money_format": f"${money:,.2f}",
        }

    @staticmethod
    def string_regex() -> dict:
        """
        Demonstrate regular expression operations on strings.
        
        Returns:
            dict: Dictionary with regex results.
        """
        text = "Hello 123 World 456"
        email = "test@example.com"
        
        return {
            "findall_digits": re.findall(r"\d+", text),
            "findall_words": re.findall(r"[A-Z]\w+", text),
            "search": bool(re.search(r"\d{3}", text)),
            "match": bool(re.match(r"Hello", text)),
            "sub": re.sub(r"\d", "X", text),
            "split_by_digits": re.split(r"\d+", text),
            "email_valid": bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)),
        }

    @staticmethod
    def string_immutability() -> dict:
        """
        Demonstrate string immutability in Python.
        
        Returns:
            dict: Dictionary showing immutability behavior.
        """
        text = "Hello"
        modified = text.replace("H", "J")
        
        return {
            "original_unchanged": text,
            "returns_new_string": modified,
            "are_different_objects": text is not modified,
            "both_valid": f"text={text}, modified={modified}",
        }

    @staticmethod
    def string_special_characters() -> dict:
        """
        Demonstrate special characters and escape sequences in strings.
        
        Returns:
            dict: Dictionary with special characters.
        """
        return {
            "newline": "Line 1\nLine 2",
            "tab": "Col1\tCol2\tCol3",
            "backslash": "C:\\Users\\name",
            "quote": 'He said "Hello"',
            "unicode": "Hello \u0041 \u03B1 \u4E2D",
            "raw_backslash": r"C:\Users\name",
        }
