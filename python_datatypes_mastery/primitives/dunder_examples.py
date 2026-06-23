"""
Dunder method demonstrations and `Employee` example class.

Shows how operator syntax maps to special (dunder) methods.
"""
from __future__ import annotations

from typing import Any


class Employee:
    """
    Simple Employee class that demonstrates dunder methods.

    Attributes:
        name: Employee name.
        salary: Numeric salary for the employee.
    """

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = float(salary)

    def __add__(self, other: "Employee") -> "Employee":
        """
        Add two employees by producing a combined pseudo-employee.

        This is educational: adding employees returns a new `Employee` with
        combined name and summed salary.
        """
        combined_name = f"{self.name}&{other.name}"
        return Employee(combined_name, self.salary + other.salary)

    def __str__(self) -> str:
        """Readable string for printing."""
        return f"Employee(name={self.name}, salary={self.salary:.2f})"

    def __repr__(self) -> str:
        """Unambiguous representation helpful for debugging."""
        return f"Employee(name={self.name!r}, salary={self.salary!r})"


def demo_dunders() -> None:
    """Demonstrate several built-in dunder behaviors in simple prints."""
    a = [1, 2]
    b = [3]
    print("append via method:", end=" ")
    a.append(4)
    print(a)

    print("addition maps to __add__ (numbers):", 1 + 2)
    print("length maps to __len__:", len(a))
    print("contains maps to __contains__:", 2 in a)
    print("absolute maps to __abs__ (numbers):", abs(-5))
