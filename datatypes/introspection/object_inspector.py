"""
Object Inspector

Comprehensive tool for inspecting Python objects and their properties.
"""

from typing import Dict, List, Any, Callable
import inspect


class ObjectInspector:
    """Advanced object inspection utilities."""

    @staticmethod
    def inspect_object(obj: Any) -> Dict[str, Any]:
        """
        Get comprehensive information about an object.
        
        Args:
            obj: Object to inspect.
            
        Returns:
            Dict[str, Any]: Dictionary with object information.
        """
        return {
            "type": type(obj).__name__,
            "id": id(obj),
            "dir_count": len(dir(obj)),
            "has_dict": hasattr(obj, "__dict__"),
            "is_callable": callable(obj),
            "module": type(obj).__module__,
        }

    @staticmethod
    def get_attributes(obj: Any) -> Dict[str, List[str]]:
        """
        Get categorized attributes of an object.
        
        Args:
            obj: Object to inspect.
            
        Returns:
            Dict[str, List[str]]: Categorized attributes.
        """
        all_attrs = dir(obj)
        
        return {
            "public_attributes": [a for a in all_attrs if not a.startswith('_')],
            "private_attributes": [a for a in all_attrs if a.startswith('_') and not a.startswith('__')],
            "dunder_attributes": [a for a in all_attrs if a.startswith('__') and a.endswith('__')],
            "methods": [a for a in all_attrs if callable(getattr(obj, a, None))],
            "properties": [a for a in all_attrs if not callable(getattr(obj, a, None)) and not a.startswith('_')],
        }

    @staticmethod
    def inspect_function(func: Callable) -> Dict[str, Any]:
        """
        Inspect a function's properties.
        
        Args:
            func: Function to inspect.
            
        Returns:
            Dict[str, Any]: Function information.
        """
        try:
            sig = inspect.signature(func)
            source = inspect.getsource(func)
            is_builtin = inspect.isbuiltin(func)
        except (ValueError, OSError, TypeError):
            sig = None
            source = "N/A"
            is_builtin = True
        
        return {
            "name": func.__name__,
            "signature": str(sig) if sig else "N/A",
            "module": func.__module__ if hasattr(func, '__module__') else "N/A",
            "is_builtin": is_builtin,
            "is_method": inspect.ismethod(func),
            "is_function": inspect.isfunction(func),
            "docstring": func.__doc__,
        }

    @staticmethod
    def inspect_class(cls: type) -> Dict[str, Any]:
        """
        Inspect a class's properties.
        
        Args:
            cls: Class to inspect.
            
        Returns:
            Dict[str, Any]: Class information.
        """
        return {
            "name": cls.__name__,
            "module": cls.__module__,
            "bases": [base.__name__ for base in cls.__bases__],
            "is_abstract": inspect.isabstract(cls),
            "methods": [m for m in dir(cls) if callable(getattr(cls, m)) and not m.startswith('_')],
            "mro": [c.__name__ for c in inspect.getmro(cls)],
            "docstring": cls.__doc__,
        }

    @staticmethod
    def get_object_memory_info(obj: Any) -> Dict[str, Any]:
        """
        Get memory-related information about an object.
        
        Args:
            obj: Object to inspect.
            
        Returns:
            Dict[str, Any]: Memory information.
        """
        import sys
        
        return {
            "id": id(obj),
            "size_bytes": sys.getsizeof(obj),
            "type": type(obj).__name__,
            "ref_count": sys.getrefcount(obj),
        }

    @staticmethod
    def compare_types(obj1: Any, obj2: Any) -> Dict[str, Any]:
        """
        Compare types of two objects.
        
        Args:
            obj1: First object.
            obj2: Second object.
            
        Returns:
            Dict[str, Any]: Comparison results.
        """
        return {
            "obj1_type": type(obj1).__name__,
            "obj2_type": type(obj2).__name__,
            "same_type": type(obj1) == type(obj2),
            "obj1_isinstance_obj2_type": isinstance(obj1, type(obj2)),
            "obj2_isinstance_obj1_type": isinstance(obj2, type(obj1)),
        }

    @staticmethod
    def find_methods_with_pattern(obj: Any, pattern: str) -> List[str]:
        """
        Find methods matching a pattern.
        
        Args:
            obj: Object to search.
            pattern: Pattern to match (case-insensitive).
            
        Returns:
            List[str]: Matching method names.
        """
        all_attrs = dir(obj)
        pattern_lower = pattern.lower()
        
        return [
            attr for attr in all_attrs
            if pattern_lower in attr.lower() and callable(getattr(obj, attr, None))
        ]

    @staticmethod
    def get_mutable_immutable_info() -> Dict[str, Dict[str, bool]]:
        """
        Information about mutability of built-in types.
        
        Returns:
            Dict[str, Dict[str, bool]]: Mutability information.
        """
        return {
            "immutable_types": {
                "int": True,
                "float": True,
                "str": True,
                "tuple": True,
                "bool": True,
                "frozenset": True,
            },
            "mutable_types": {
                "list": True,
                "dict": True,
                "set": True,
                "bytearray": True,
            },
        }
