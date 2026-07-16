"""
Patient Model

This module defines the Pydantic model for Patient data.
Pydantic is used for data validation and JSON serialization.
"""

from pydantic import BaseModel, Field
from typing import Optional


class Patient(BaseModel):
    """
    Patient model representing a hospital patient.
    
    Type hints are used here to ensure type safety and enable IDEs to
    provide better autocomplete and error checking.
    """
    
    id: int = Field(..., description="Unique patient identifier")
    name: str = Field(..., min_length=1, description="Patient's full name")
    age: int = Field(..., ge=0, le=150, description="Patient's age")
    gender: str = Field(..., description="Patient's gender (Male/Female/Other)")
    phone: str = Field(..., min_length=10, description="Patient's phone number")
    
    def to_dict(self) -> dict:
        """Convert patient object to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "phone": self.phone
        }
    
    class Config:
        """Configuration for Pydantic model."""
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "John Doe",
                "age": 30,
                "gender": "Male",
                "phone": "9876543210"
            }
        }


class PatientUpdate(BaseModel):
    """
    Model for updating patient information.
    All fields are optional so users can update only what they need.
    """
    
    name: Optional[str] = Field(None, min_length=1, description="Patient's full name")
    age: Optional[int] = Field(None, ge=0, le=150, description="Patient's age")
    gender: Optional[str] = Field(None, description="Patient's gender")
    phone: Optional[str] = Field(None, min_length=10, description="Patient's phone number")
