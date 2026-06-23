"""
Classes Module

This module demonstrates object-oriented programming concepts:
classes, inheritance, composition, and class management.
"""

from .student import Student
from .employee import Employee
from .department import Department
from .composition import Company, Address
from .class_manager import ClassManager

__all__ = [
    "Student",
    "Employee",
    "Department",
    "Company",
    "Address",
    "ClassManager",
]
