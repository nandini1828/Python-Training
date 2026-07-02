"""Test suite for Department class."""
import pytest
from datatypes.classes import Department, Employee


class TestDepartment:
    def test_department_creation(self):
        dept = Department("Engineering", "E001", 500000)
        assert dept.name == "Engineering"
        assert dept.manager_id == "E001"
        assert dept.budget == 500000
    
    def test_add_employee(self):
        dept = Department("Engineering", "E001")
        emp = Employee("E002", "Alice", "Developer", 100000)
        assert dept.add_employee(emp) is True
        assert len(dept.employees) == 1
    
    def test_get_payroll(self):
        dept = Department("Engineering", "E001", 500000)
        emp1 = Employee("E001", "Alice", "Developer", 100000)
        emp2 = Employee("E002", "Bob", "Designer", 80000)
        dept.add_employee(emp1)
        dept.add_employee(emp2)
        assert dept.get_payroll() == 180000
    
    def test_over_budget(self):
        dept = Department("Engineering", "E001", 100000)
        emp = Employee("E002", "Alice", "Developer", 120000)
        dept.add_employee(emp)
        assert dept.is_over_budget() is True
