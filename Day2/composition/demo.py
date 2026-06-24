from __future__ import annotations

from composition.composition_utils import Company, Department, Employee


def run_composition_demo() -> None:
    """Show a simple composition example with classes."""

    employee = Employee("Ada", "Teacher")
    department = Department("School", [employee])
    company = Company("Bright Future", [department])

    print("Company:", company.name)
    print("Department:", company.departments[0].name)
    print("Employee:", company.departments[0].employees[0].name)
