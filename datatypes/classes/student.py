"""
Student Class

Demonstrates basic class creation with attributes and methods.
"""

from typing import Optional, Dict, List
from datetime import datetime, date


class Student:
    """
    Represents a student with academic information.
    
    Attributes:
        student_id: Unique student identifier.
        name: Full name of the student.
        gpa: Grade point average.
        major: Field of study.
        enrollment_date: Date of enrollment.
        courses: List of courses enrolled in.
    """
    
    # Class variable - shared by all instances
    institution = "Python University"
    total_students = 0
    
    def __init__(self, student_id: str, name: str, major: str, 
                 gpa: float = 0.0):
        """
        Initialize a Student instance.
        
        Args:
            student_id: Unique identifier for the student.
            name: Full name of the student.
            major: Field of study.
            gpa: Initial GPA (default 0.0).
        """
        self.student_id = student_id
        self.name = name
        self.major = major
        self.gpa = gpa
        self.enrollment_date = datetime.now()
        self.courses: List[str] = []
        
        Student.total_students += 1
    
    def enroll_course(self, course_name: str) -> bool:
        """
        Enroll student in a course.
        
        Args:
            course_name: Name of the course.
            
        Returns:
            bool: True if successful, False if already enrolled.
        """
        if course_name not in self.courses:
            self.courses.append(course_name)
            return True
        return False
    
    def drop_course(self, course_name: str) -> bool:
        """
        Drop a course.
        
        Args:
            course_name: Name of the course to drop.
            
        Returns:
            bool: True if successful, False if not enrolled.
        """
        if course_name in self.courses:
            self.courses.remove(course_name)
            return True
        return False
    
    def update_gpa(self, new_gpa: float) -> None:
        """
        Update student's GPA.
        
        Args:
            new_gpa: New GPA value.
            
        Raises:
            ValueError: If GPA is not between 0 and 4.0.
        """
        if not (0 <= new_gpa <= 4.0):
            raise ValueError("GPA must be between 0 and 4.0")
        self.gpa = new_gpa
    
    def is_on_honor_roll(self) -> bool:
        """
        Check if student is on honor roll (GPA >= 3.5).
        
        Returns:
            bool: True if on honor roll, False otherwise.
        """
        return self.gpa >= 3.5
    
    def get_courses_info(self) -> Dict[str, object]:
        """
        Get course information.
        
        Returns:
            Dict[str, object]: Course enrollment details.
        """
        return {
            "course_count": len(self.courses),
            "courses": self.courses,
            "enrolled": len(self.courses) > 0,
        }
    
    def get_info(self) -> Dict[str, object]:
        """
        Get complete student information.
        
        Returns:
            Dict[str, object]: All student information.
        """
        return {
            "student_id": self.student_id,
            "name": self.name,
            "major": self.major,
            "gpa": self.gpa,
            "enrollment_date": self.enrollment_date,
            "courses": self.courses,
            "course_count": len(self.courses),
            "on_honor_roll": self.is_on_honor_roll(),
        }
    
    def __str__(self) -> str:
        """String representation."""
        return f"Student({self.student_id}, {self.name}, {self.major})"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (f"Student(student_id='{self.student_id}', name='{self.name}', "
                f"major='{self.major}', gpa={self.gpa})")
    
    @classmethod
    def get_total_students(cls) -> int:
        """
        Get total number of students created.
        
        Returns:
            int: Total student count.
        """
        return cls.total_students
    
    @classmethod
    def get_institution(cls) -> str:
        """
        Get institution name.
        
        Returns:
            str: Institution name.
        """
        return cls.institution
    
    @staticmethod
    def is_valid_gpa(gpa: float) -> bool:
        """
        Validate GPA value.
        
        Args:
            gpa: GPA to validate.
            
        Returns:
            bool: True if valid, False otherwise.
        """
        return isinstance(gpa, (int, float)) and 0 <= gpa <= 4.0
