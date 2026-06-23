class Box:
    """
    A simple class to demonstrate dunder methods and operator overloading.
    """

    def __init__(self, value):
        self.value = value

    # -------------------------
    # STRING REPRESENTATION
    # -------------------------

    def __str__(self):
        """Human-readable output."""
        return f"Box({self.value})"

    def __repr__(self):
        """Developer-friendly output."""
        return f"Box(value={self.value})"

    # -------------------------
    # ARITHMETIC OPERATIONS
    # -------------------------

    def __add__(self, other):
        """Addition using + operator."""
        return Box(self.value + other.value)

    def __sub__(self, other):
        """Subtraction using - operator."""
        return Box(self.value - other.value)

    def __mul__(self, other):
        """Multiplication using * operator."""
        return Box(self.value * other.value)

    # -------------------------
    # COMPARISON OPERATIONS
    # -------------------------

    def __eq__(self, other):
        """Equality check using ==."""
        return self.value == other.value

    def __lt__(self, other):
        """Less than comparison."""
        return self.value < other.value

    def __gt__(self, other):
        """Greater than comparison."""
        return self.value > other.value

    # -------------------------
    # LENGTH (optional concept demo)
    # -------------------------

    def __len__(self):
        """Length of value if supported."""
        return len(str(self.value))
    