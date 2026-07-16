"""
Doctor Model

This module defines the Pydantic model for Doctor data.
"""

from pydantic import BaseModel, Field
from typing import Optional


class Doctor(BaseModel):
    """
    Doctor model representing a hospital doctor.
    
    Type hints help ensure type safety and enable better development experience.
    """
    
    id: int = Field(..., description="Unique doctor identifier")
    name: str = Field(..., min_length=1, description="Doctor's full name")
    specialization: str = Field(..., min_length=1, description="Doctor's medical specialization")
    experience: int = Field(..., ge=0, le=60, description="Doctor's years of experience")
    
    def to_dict(self) -> dict:
        """Convert doctor object to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "specialization": self.specialization,
            "experience": self.experience
        }
    
    class Config:
        """Configuration for Pydantic model."""
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Dr. Smith",
                "specialization": "Cardiology",
                "experience": 10
            }
        }


class DoctorUpdate(BaseModel):
    """
    Model for updating doctor information.
    All fields are optional for flexible updates.
    """
    
    name: Optional[str] = Field(None, min_length=1, description="Doctor's full name")
    specialization: Optional[str] = Field(None, min_length=1, description="Doctor's specialization")
    experience: Optional[int] = Field(None, ge=0, le=60, description="Doctor's years of experience")
