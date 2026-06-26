"""
dir() Function Examples

Demonstrates using dir() to list attributes and methods
of objects and modules.
"""

from typing import List, Dict


class DirectoryExamples:
    """Examples of using the dir() function for introspection."""

    @staticmethod
    def dir_of_string() -> List[str]:
        """
        Get directory of a string object.
        
        Returns:
            List[str]: List of string attributes and methods.
        """
        return dir("hello")

    @staticmethod
    def dir_of_list() -> List[str]:
        """
        Get directory of a list object.
        
        Returns:
            List[str]: List of list attributes and methods.
        """
        return dir([1, 2, 3])

    @staticmethod
    def dir_of_dict() -> List[str]:
        """
        Get directory of a dictionary object.
        
        Returns:
            List[str]: List of dict attributes and methods.
        """
        return dir({})

    @staticmethod
    def dir_of_integer() -> List[str]:
        """
        Get directory of an integer object.
        
        Returns:
            List[str]: List of integer attributes and methods.
        """
        return dir(42)

    @staticmethod
    def dir_filtering() -> Dict[str, list]:
        """
        Demonstrate filtering dir() results.
        
        Returns:
            Dict[str, list]: Dictionary with filtered results.
        """
        text = "hello"
        all_attrs = dir(text)
        
        return {
            "all_attributes_count": len(all_attrs),
            "public_methods": [attr for attr in all_attrs if not attr.startswith('_')],
            "dunder_methods": [attr for attr in all_attrs if attr.startswith('__')],
            "private_methods": [attr for attr in all_attrs if attr.startswith('_') and not attr.startswith('__')],
            "specific_method": [attr for attr in all_attrs if 'upper' in attr.lower()],
        }

    @staticmethod
    def dir_comparison() -> Dict[str, int]:
        """
        Compare dir() results between different types.
        
        Returns:
            Dict[str, int]: Comparison of attribute counts.
        """
        return {
            "string_attrs": len(dir("")),
            "list_attrs": len(dir([])),
            "dict_attrs": len(dir({})),
            "set_attrs": len(dir(set())),
            "tuple_attrs": len(dir(())),
            "int_attrs": len(dir(0)),
            "float_attrs": len(dir(0.0)),
            "bool_attrs": len(dir(True)),
        }

    @staticmethod
    def find_callable_methods() -> Dict[str, list]:
        """
        Find callable methods in an object.
        
        Returns:
            Dict[str, list]: Dictionary with callable methods.
        """
        text = "hello"
        all_attrs = dir(text)
        
        return {
            "callable_methods": [
                attr for attr in all_attrs 
                if callable(getattr(text, attr))
            ],
            "string_callable_count": len([
                attr for attr in all_attrs 
                if callable(getattr(text, attr))
            ]),
        }
