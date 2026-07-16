"""Appointment API routes."""

from fastapi import APIRouter

from app.models.appointment import AppointmentCreate
from app.services.appointment_service import (
    book_appointment,
    delete_appointment,
    get_all_appointments,
    get_patient_appointments,
    get_recent_appointments,
)

router = APIRouter(prefix="/appointments", tags=["Appointments"])


@router.get("/")
def view_appointments():
    return get_all_appointments()


@router.get("/recent")
def recent_appointments():
    return get_recent_appointments()


@router.get("/patient/{patient_id}")
def patient_appointments(patient_id: int):
    return get_patient_appointments(patient_id)


@router.post("/")
def create_appointment(appointment: AppointmentCreate):
    return book_appointment(
        patient_id=appointment.patient_id,
        doctor_id=appointment.doctor_id,
        appointment_date=appointment.appointment_date.isoformat(),
    )


@router.delete("/{appointment_id}")
def remove_appointment(appointment_id: int):
    return delete_appointment(appointment_id)