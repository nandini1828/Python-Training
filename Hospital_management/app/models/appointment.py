"""Appointment models."""

from datetime import date

from pydantic import BaseModel, Field


class AppointmentCreate(BaseModel):
    """Simple request schema for creating an appointment."""

    patient_id: int
    doctor_id: int
    appointment_date: date = Field(
        ...,
        description="Appointment date in YYYY-MM-DD format",
    )


class Appointment:
    """Represents a hospital appointment."""

    def __init__(
        self,
        appointment_id: int,
        patient_id: int,
        doctor_id: int,
        appointment_date: str,
    ):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date

    def __str__(self) -> str:
        return (
            f"Appointment("
            f"ID={self.appointment_id}, "
            f"Patient ID={self.patient_id}, "
            f"Doctor ID={self.doctor_id}, "
            f"Date='{self.appointment_date}')"
        )