"""Test suite for ClassManager."""
import pytest
from app.classes import ClassManager


class TestClassManager:
    def test_manager_initialization(self):
        manager = ClassManager()
        assert len(manager.students) == 0
        assert len(manager.employees) == 0
    
    def test_create_student(self):
        manager = ClassManager()
        student = manager.create_student("S001", "Alice", "CS", 3.8)
        assert len(manager.students) == 1
        assert student.name == "Alice"
    
    def test_get_demo_data(self):
        manager = ClassManager()
        data = manager.get_demo_data()
        assert "students" in data
        assert "employees" in data
        assert len(data["students"]) > 0
    
    def test_get_summary(self):
        manager = ClassManager()
        manager.get_demo_data()
        summary = manager.get_summary()
        assert summary["total_students"] > 0
        assert summary["total_employees"] > 0
