"""Employee model for the employee management system."""

from dataclasses import dataclass

from app.models.address import Address


@dataclass
class Employee:
    """A simple employee object with composition for address details."""

    employee_id: str
    first_name: str
    last_name: str
    age: int
    email: str
    department_id: str
    salary: float
    address: Address

    def to_dict(self) -> dict[str, object]:
        """Return the employee record as a dictionary."""
        return {
            "employee_id": self.employee_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "department_id": self.department_id,
            "salary": self.salary,
            "address": self.address.to_dict(),
        }
