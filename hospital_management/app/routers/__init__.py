"""
Routers Module

This module imports and exports all route files.
"""

from .patient_router import router as patient_router
from .doctor_router import router as doctor_router
from .appointment_router import router as appointment_router

__all__ = ["patient_router", "doctor_router", "appointment_router"]
