"""
Hospital Management System Models

This module contains Pydantic models for the Hospital Management System.
"""

from .patient import Patient
from .doctor import Doctor
from .appointment import Appointment

__all__ = ["Patient", "Doctor", "Appointment"]
