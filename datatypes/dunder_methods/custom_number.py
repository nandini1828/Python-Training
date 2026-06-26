"""
Custom Number Class

Demonstrates operator overloading for numeric operations.
"""

from typing import Union


class CustomNumber:
    """
    A custom number class demonstrating arithmetic dunder methods.
    
    Supports: +, -, *, /, //, %, **, etc.
    """
    
    def __init__(self, value: Union[int, float]):
        """
        Initialize CustomNumber.
        
        Args:
            value: Numeric value.
        """
        self.value = float(value)
    
    def __add__(self, other) -> "CustomNumber":
        """Addition operator."""
        if isinstance(other, CustomNumber):
            return CustomNumber(self.value + other.value)
        return CustomNumber(self.value + other)
    
    def __radd__(self, other) -> "CustomNumber":
        """Right addition (for other + self)."""
        return self.__add__(other)
    
    def __sub__(self, other) -> "CustomNumber":
        """Subtraction operator."""
        if isinstance(other, CustomNumber):
            return CustomNumber(self.value - other.value)
        return CustomNumber(self.value - other)
    
    def __rsub__(self, other) -> "CustomNumber":
        """Right subtraction."""
        if isinstance(other, CustomNumber):
            return CustomNumber(other.value - self.value)
        return CustomNumber(other - self.value)
    
    def __mul__(self, other) -> "CustomNumber":
        """Multiplication operator."""
        if isinstance(other, CustomNumber):
            return CustomNumber(self.value * other.value)
        return CustomNumber(self.value * other)
    
    def __rmul__(self, other) -> "CustomNumber":
        """Right multiplication."""
        return self.__mul__(other)
    
    def __truediv__(self, other) -> "CustomNumber":
        """True division operator."""
        if isinstance(other, CustomNumber):
            if other.value == 0:
                raise ValueError("Cannot divide by zero")
            return CustomNumber(self.value / other.value)
        if other == 0:
            raise ValueError("Cannot divide by zero")
        return CustomNumber(self.value / other)
    
    def __floordiv__(self, other) -> "CustomNumber":
        """Floor division operator."""
        if isinstance(other, CustomNumber):
            return CustomNumber(self.value // other.value)
        return CustomNumber(self.value // other)
    
    def __mod__(self, other) -> "CustomNumber":
        """Modulo operator."""
        if isinstance(other, CustomNumber):
            return CustomNumber(self.value % other.value)
        return CustomNumber(self.value % other)
    
    def __pow__(self, other) -> "CustomNumber":
        """Power operator."""
        if isinstance(other, CustomNumber):
            return CustomNumber(self.value ** other.value)
        return CustomNumber(self.value ** other)
    
    def __neg__(self) -> "CustomNumber":
        """Negation operator (unary -)."""
        return CustomNumber(-self.value)
    
    def __pos__(self) -> "CustomNumber":
        """Positive operator (unary +)."""
        return CustomNumber(+self.value)
    
    def __abs__(self) -> "CustomNumber":
        """Absolute value operator."""
        return CustomNumber(abs(self.value))
    
    def __eq__(self, other) -> bool:
        """Equality comparison."""
        if isinstance(other, CustomNumber):
            return self.value == other.value
        return self.value == other
    
    def __ne__(self, other) -> bool:
        """Not equal comparison."""
        return not self.__eq__(other)
    
    def __lt__(self, other) -> bool:
        """Less than comparison."""
        if isinstance(other, CustomNumber):
            return self.value < other.value
        return self.value < other
    
    def __le__(self, other) -> bool:
        """Less than or equal comparison."""
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other) -> bool:
        """Greater than comparison."""
        if isinstance(other, CustomNumber):
            return self.value > other.value
        return self.value > other
    
    def __ge__(self, other) -> bool:
        """Greater than or equal comparison."""
        return self.__gt__(other) or self.__eq__(other)
    
    def __hash__(self) -> int:
        """Hash for use in sets and dicts."""
        return hash(self.value)
    
    def __repr__(self) -> str:
        """Developer representation."""
        return f"CustomNumber({self.value})"
    
    def __str__(self) -> str:
        """String representation."""
        return str(self.value)
    
    def __int__(self) -> int:
        """Convert to int."""
        return int(self.value)
    
    def __float__(self) -> float:
        """Convert to float."""
        return self.value
    
    def __bool__(self) -> bool:
        """Truthiness."""
        return self.value != 0.0
