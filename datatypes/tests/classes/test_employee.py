"""Test suite for Employee class."""
import pytest
from datatypes.classes import Employee


class TestEmployee:
    def test_employee_creation(self):
        emp = Employee("E001", "Alice", "Developer", 100000)
        assert emp.employee_id == "E001"
        assert emp.name == "Alice"
        assert emp.position == "Developer"
        assert emp.salary == 100000
        assert emp.is_active is True
    
    def test_give_raise(self):
        emp = Employee("E001", "Alice", "Developer", 100000)
        new_salary = emp.give_raise(10)
        assert new_salary == 110000
    
    def test_performance_review(self):
        emp = Employee("E001", "Alice", "Developer", 100000)
        emp.add_performance_review(95, "Excellent")
        assert len(emp.reviews) == 1
        assert emp.get_average_review_score() == 95.0
    
    def test_invalid_salary(self):
        with pytest.raises(ValueError):
            Employee("E001", "Alice", "Developer", 10000)
    
    def test_promote(self):
        emp = Employee("E001", "Alice", "Developer", 100000)
        emp.promote("Senior Developer", 20000)
        assert emp.position == "Senior Developer"
        assert emp.salary == 120000
