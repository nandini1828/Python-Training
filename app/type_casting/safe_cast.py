"""
Safe Type Casting

This module provides safe casting methods with error handling
and validation for type conversions.
"""

from typing import Any, Union, Optional, Callable


class SafeCast:
    """Provides safe type casting with error handling."""

    @staticmethod
    def to_int(value: Any, default: int = 0) -> int:
        """
        Safely convert a value to integer.
        
        Args:
            value: Value to convert.
            default: Default value if conversion fails.
            
        Returns:
            int: Converted integer or default value.
        """
        try:
            return int(value)
        except (ValueError, TypeError):
            return default

    @staticmethod
    def to_float(value: Any, default: float = 0.0) -> float:
        """
        Safely convert a value to float.
        
        Args:
            value: Value to convert.
            default: Default value if conversion fails.
            
        Returns:
            float: Converted float or default value.
        """
        try:
            return float(value)
        except (ValueError, TypeError):
            return default

    @staticmethod
    def to_str(value: Any, default: str = "") -> str:
        """
        Safely convert a value to string.
        
        Args:
            value: Value to convert.
            default: Default value if conversion fails.
            
        Returns:
            str: Converted string or default value.
        """
        try:
            return str(value)
        except Exception:
            return default

    @staticmethod
    def to_bool(value: Any, default: bool = False) -> bool:
        """
        Safely convert a value to boolean.
        
        Args:
            value: Value to convert.
            default: Default value if conversion fails.
            
        Returns:
            bool: Converted boolean or default value.
        """
        try:
            return bool(value)
        except Exception:
            return default

    @staticmethod
    def to_list(value: Any, default: Optional[list] = None) -> list:
        """
        Safely convert a value to list.
        
        Args:
            value: Value to convert.
            default: Default value if conversion fails.
            
        Returns:
            list: Converted list or default value.
        """
        if default is None:
            default = []
        try:
            if isinstance(value, list):
                return value
            elif isinstance(value, (tuple, set)):
                return list(value)
            elif isinstance(value, dict):
                return list(value.values())
            elif isinstance(value, str):
                return [value]
            else:
                return [value]
        except Exception:
            return default

    @staticmethod
    def to_dict(value: Any, default: Optional[dict] = None) -> dict:
        """
        Safely convert a value to dictionary.
        
        Args:
            value: Value to convert.
            default: Default value if conversion fails.
            
        Returns:
            dict: Converted dictionary or default value.
        """
        if default is None:
            default = {}
        try:
            if isinstance(value, dict):
                return value
            else:
                return default
        except Exception:
            return default

    @staticmethod
    def validate_and_cast(value: Any, target_type: type, 
                         validation_func: Optional[Callable] = None) -> Union[Any, None]:
        """
        Cast with optional validation function.
        
        Args:
            value: Value to convert.
            target_type: Target type for conversion.
            validation_func: Optional validation function.
            
        Returns:
            Union[Any, None]: Converted value or None if validation fails.
        """
        try:
            converted = target_type(value)
            if validation_func is None or validation_func(converted):
                return converted
            return None
        except Exception:
            return None

    @staticmethod
    def cast_or_raise(value: Any, target_type: type) -> Any:
        """
        Cast with exception raising on failure.
        
        Args:
            value: Value to convert.
            target_type: Target type for conversion.
            
        Returns:
            Any: Converted value.
            
        Raises:
            TypeError: If conversion fails.
        """
        try:
            return target_type(value)
        except Exception as e:
            raise TypeError(f"Cannot cast {value!r} to {target_type.__name__}") from e

    @staticmethod
    def attempt_cast(value: Any, *target_types) -> Optional[Any]:
        """
        Try casting with multiple target types, return first successful conversion.
        
        Args:
            value: Value to convert.
            *target_types: Multiple target types to try.
            
        Returns:
            Optional[Any]: First successful conversion or None.
        """
        for target_type in target_types:
            try:
                return target_type(value)
            except Exception:
                continue
        return None
