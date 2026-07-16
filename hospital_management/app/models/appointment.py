"""
Appointment Model

This module defines the Pydantic model for Appointment data.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Appointment(BaseModel):
    """
    Appointment model representing a hospital appointment.
    
    This demonstrates datetime validation in Pydantic models.
    """
    
    id: int = Field(..., description="Unique appointment identifier")
    patient_id: int = Field(..., description="ID of the patient")
    doctor_id: int = Field(..., description="ID of the doctor")
    appointment_date: datetime = Field(..., description="Date and time of appointment")
    status: str = Field(default="Scheduled", description="Appointment status")
    
    def to_dict(self) -> dict:
        """Convert appointment object to dictionary."""
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "appointment_date": self.appointment_date,
            "status": self.status
        }
    
    class Config:
        """Configuration for Pydantic model."""
        json_schema_extra = {
            "example": {
                "id": 1,
                "patient_id": 1,
                "doctor_id": 1,
                "appointment_date": "2024-12-25T10:00:00",
                "status": "Scheduled"
            }
        }


class AppointmentCreate(BaseModel):
    """
    Model for creating a new appointment.
    Only requires the essential fields - ID is auto-generated.
    """
    
    patient_id: int = Field(..., description="ID of the patient")
    doctor_id: int = Field(..., description="ID of the doctor")
    appointment_date: datetime = Field(..., description="Date and time of appointment")


class AppointmentUpdate(BaseModel):
    """
    Model for updating appointment status.
    Used when cancelling or rescheduling appointments.
    """
    
    status: Optional[str] = Field(None, description="New status for appointment")
    appointment_date: Optional[datetime] = Field(None, description="New date and time if rescheduling")
