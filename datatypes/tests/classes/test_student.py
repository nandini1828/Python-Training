"""Test suite for Student class."""
import pytest
from datatypes.classes import Student


class TestStudent:
    def test_student_creation(self):
        student = Student("S001", "Alice", "Computer Science", 3.8)
        assert student.student_id == "S001"
        assert student.name == "Alice"
        assert student.major == "Computer Science"
        assert student.gpa == 3.8
    
    def test_enroll_course(self):
        student = Student("S001", "Alice", "CS", 3.5)
        assert student.enroll_course("Python") is True
        assert student.enroll_course("Python") is False
        assert len(student.courses) == 1
    
    def test_honor_roll(self):
        student1 = Student("S001", "Alice", "CS", 3.8)
        student2 = Student("S002", "Bob", "IT", 3.2)
        assert student1.is_on_honor_roll() is True
        assert student2.is_on_honor_roll() is False
    
    def test_update_gpa(self):
        student = Student("S001", "Alice", "CS", 3.5)
        student.update_gpa(3.9)
        assert student.gpa == 3.9
        
        with pytest.raises(ValueError):
            student.update_gpa(4.5)
