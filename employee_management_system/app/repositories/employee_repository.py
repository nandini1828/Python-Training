"""Simple repository for reading and writing employee records from JSON files."""

import csv
import json
from pathlib import Path

from app.config.settings import DEPARTMENTS_JSON_PATH, EMPLOYEES_CSV_PATH, EMPLOYEES_JSON_PATH
from app.models.address import Address
from app.models.department import Department
from app.models.employee import Employee


class EmployeeRepository:
    """Repository that stores employees in JSON and exports CSV."""

    def __init__(self, file_path: Path = EMPLOYEES_JSON_PATH) -> None:
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        """Create empty data file if missing."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")

    def _read_json(self) -> list[dict[str, object]]:
        """Read all employee records from JSON."""
        with self.file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def _write_json(self, employees: list[dict[str, object]]) -> None:
        """Write employee records to JSON."""
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(employees, file, indent=4)

    def list_employees(self) -> list[Employee]:
        """Return all employees as Employee objects."""
        records = self._read_json()
        return [self._record_to_employee(record) for record in records]

    def add_employee(self, employee: Employee) -> None:
        """Store a new employee record."""
        records = self._read_json()
        records.append(employee.to_dict())
        self._write_json(records)

    def get_employee_by_id(self, employee_id: str) -> Employee | None:
        """Look up an employee by id."""
        for record in self._read_json():
            if record.get("employee_id") == employee_id:
                return self._record_to_employee(record)
        return None

    def update_employee(self, employee: Employee) -> None:
        """Replace an employee record with a new object."""
        records = self._read_json()
        for index, record in enumerate(records):
            if record.get("employee_id") == employee.employee_id:
                records[index] = employee.to_dict()
                self._write_json(records)
                return
        raise ValueError(f"Employee with id {employee.employee_id} was not found")

    def delete_employee(self, employee_id: str) -> bool:
        """Delete an employee record if it exists."""
        records = self._read_json()
        filtered = [record for record in records if record.get("employee_id") != employee_id]
        if len(filtered) == len(records):
            return False
        self._write_json(filtered)
        return True

    def search_employees(self, keyword: str) -> list[Employee]:
        """Search employees by name or department id."""
        keyword = keyword.lower()
        matches: list[Employee] = []
        for record in self._read_json():
            text = " ".join(
                [
                    str(record.get("first_name", "")),
                    str(record.get("last_name", "")),
                    str(record.get("email", "")),
                    str(record.get("department_id", "")),
                ]
            ).lower()
            if keyword in text:
                matches.append(self._record_to_employee(record))
        return matches

    def filter_employees(self, department_id: str | None = None, minimum_salary: float | None = None) -> list[Employee]:
        """Filter employees by department id and minimum salary."""
        matches: list[Employee] = []
        for record in self._read_json():
            if department_id and record.get("department_id") != department_id:
                continue
            if minimum_salary is not None and float(record.get("salary", 0)) < minimum_salary:
                continue
            matches.append(self._record_to_employee(record))
        return matches

    def export_to_csv(self) -> None:
        """Export all employees to the CSV file."""
        employees = self.list_employees()
        with EMPLOYEES_CSV_PATH.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "employee_id",
                    "first_name",
                    "last_name",
                    "age",
                    "email",
                    "department_id",
                    "salary",
                    "city",
                    "state",
                    "country",
                    "postal_code",
                ],
            )
            writer.writeheader()
            for employee in employees:
                row = employee.to_dict()
                address = row["address"]
                row.update(address)
                writer.writerow(row)

    def list_departments(self) -> list[Department]:
        """Return department records from JSON."""
        with DEPARTMENTS_JSON_PATH.open("r", encoding="utf-8") as file:
            departments = json.load(file)
        return [Department(**department) for department in departments]

    @staticmethod
    def _record_to_employee(record: dict[str, object]) -> Employee:
        """Convert a raw dictionary record into an Employee object."""
        address = Address(
            city=str(record["address"]["city"]),
            state=str(record["address"]["state"]),
            country=str(record["address"]["country"]),
            postal_code=str(record["address"]["postal_code"]),
        )
        return Employee(
            employee_id=str(record["employee_id"]),
            first_name=str(record["first_name"]),
            last_name=str(record["last_name"]),
            age=int(record["age"]),
            email=str(record["email"]),
            department_id=str(record["department_id"]),
            salary=float(record["salary"]),
            address=address,
        )
