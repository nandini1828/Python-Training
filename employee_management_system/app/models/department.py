"""Department model for the employee management system."""

from dataclasses import dataclass


@dataclass
class Department:
    """A department in the company."""

    department_id: str
    name: str
    manager: str | None = None

    def to_dict(self) -> dict[str, str | None]:
        """Return a department as a dictionary."""
        return {
            "department_id": self.department_id,
            "name": self.name,
            "manager": self.manager,
        }
