"""Employee CRUD operations backed by JSON data."""

import json
from pathlib import Path
from typing import List

from config.settings import DATA_DIR
from models.employee import Employee


class EmployeeService:
    """Simple employee service with file-backed persistence."""

    def __init__(self) -> None:
        self._employees: List[Employee] = []
        self._data_file = Path(DATA_DIR) / "employees.json"
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        self._data_file.parent.mkdir(parents=True, exist_ok=True)
        if self._data_file.exists():
            payload = json.loads(self._data_file.read_text(encoding="utf-8"))
            self._employees = [Employee(**item) for item in payload]
            return

        self._employees = [
            Employee(1, "Alice", "Engineering", 7000, "Manager"),
            Employee(2, "Bob", "HR", 6000, "Employee"),
        ]
        self._save_to_disk()

    def _save_to_disk(self) -> None:
        payload = [
            {
                "employee_id": employee.employee_id,
                "name": employee.name,
                "department": employee.department,
                "salary": employee.salary,
                "role": employee.role,
            }
            for employee in self._employees
        ]
        self._data_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def add_employee(self, employee: Employee) -> Employee:
        self._employees.append(employee)
        self._save_to_disk()
        return employee

    def list_employees(self) -> List[Employee]:
        return self._employees

    def get_employee(self, employee_id: int) -> Employee | None:
        for employee in self._employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def update_employee(self, employee_id: int, **updates: object) -> Employee | None:
        employee = self.get_employee(employee_id)
        if employee is None:
            return None

        for field, value in updates.items():
            if value is None:
                continue
            setattr(employee, field, value)

        self._save_to_disk()
        return employee

    def delete_employee(self, employee_id: int) -> bool:
        employee = self.get_employee(employee_id)
        if employee is None:
            return False
        self._employees = [item for item in self._employees if item.employee_id != employee_id]
        self._save_to_disk()
        return True

    def assign_role(self, employee_id: int, role: str) -> Employee | None:
        employee = self.get_employee(employee_id)
        if employee is None:
            return None
        employee.role = role
        self._save_to_disk()
        return employee

    def get_employees_by_role(self, role: str) -> List[Employee]:
        return [employee for employee in self._employees if employee.role.lower() == role.lower()]


employee_service = EmployeeService()


def get_employee_service() -> EmployeeService:
    return employee_service
