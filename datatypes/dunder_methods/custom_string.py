"""
Custom String Class

Demonstrates operator overloading for string-like operations.
"""


class CustomString:
    """
    A custom string class demonstrating string dunder methods.
    
    Supports: +, *, [], len(), str(), etc.
    """
    
    def __init__(self, value: str = ""):
        """
        Initialize CustomString.
        
        Args:
            value: String value.
        """
        self.value = str(value)
    
    def __add__(self, other) -> "CustomString":
        """Concatenation operator (+)."""
        if isinstance(other, CustomString):
            return CustomString(self.value + other.value)
        return CustomString(self.value + str(other))
    
    def __radd__(self, other) -> "CustomString":
        """Right concatenation."""
        return CustomString(str(other) + self.value)
    
    def __mul__(self, times: int) -> "CustomString":
        """Repetition operator (*)."""
        if not isinstance(times, int):
            raise TypeError("Can only multiply by integers")
        return CustomString(self.value * times)
    
    def __rmul__(self, times: int) -> "CustomString":
        """Right multiplication."""
        return self.__mul__(times)
    
    def __len__(self) -> int:
        """Length of string."""
        return len(self.value)
    
    def __getitem__(self, index) -> str:
        """Indexing and slicing support."""
        return self.value[index]
    
    def __setitem__(self, index, value) -> None:
        """Setting by index (converts to list since str is immutable)."""
        value_list = list(self.value)
        value_list[index] = str(value)
        self.value = "".join(value_list)
    
    def __contains__(self, item) -> bool:
        """Membership test (in operator)."""
        return str(item) in self.value
    
    def __eq__(self, other) -> bool:
        """Equality comparison."""
        if isinstance(other, CustomString):
            return self.value == other.value
        return self.value == str(other)
    
    def __ne__(self, other) -> bool:
        """Not equal comparison."""
        return not self.__eq__(other)
    
    def __lt__(self, other) -> bool:
        """Less than comparison."""
        if isinstance(other, CustomString):
            return self.value < other.value
        return self.value < str(other)
    
    def __le__(self, other) -> bool:
        """Less than or equal."""
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other) -> bool:
        """Greater than comparison."""
        if isinstance(other, CustomString):
            return self.value > other.value
        return self.value > str(other)
    
    def __ge__(self, other) -> bool:
        """Greater than or equal."""
        return self.__gt__(other) or self.__eq__(other)
    
    def __hash__(self) -> int:
        """Hash for use in sets and dicts."""
        return hash(self.value)
    
    def __repr__(self) -> str:
        """Developer representation."""
        return f"CustomString('{self.value}')"
    
    def __str__(self) -> str:
        """String representation."""
        return self.value
    
    def __iter__(self):
        """Allow iteration."""
        return iter(self.value)
    
    def __reversed__(self):
        """Reversed iteration."""
        return reversed(self.value)
    
    def __bool__(self) -> bool:
        """Truthiness - empty string is False."""
        return len(self.value) > 0
    
    def upper(self) -> "CustomString":
        """Return uppercase version."""
        return CustomString(self.value.upper())
    
    def lower(self) -> "CustomString":
        """Return lowercase version."""
        return CustomString(self.value.lower())
    
    def reverse(self) -> "CustomString":
        """Return reversed string."""
        return CustomString(self.value[::-1])
