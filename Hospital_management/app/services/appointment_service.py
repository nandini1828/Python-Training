"""Appointment service layer."""

from app.data import appointments, doctors, patients
from app.models.appointment import Appointment
from app.utils import get_next_id


def book_appointment(patient_id: int, doctor_id: int, appointment_date: str):
    if patient_id not in patients:
        return {"message": "Patient not found"}
    if doctor_id not in doctors:
        return {"message": "Doctor not found"}

    appointment_id = get_next_id(appointments)
    appointment = Appointment(
        appointment_id=appointment_id,
        patient_id=patient_id,
        doctor_id=doctor_id,
        appointment_date=appointment_date,
    )
    appointments.append(appointment)
    return {"message": "Appointment booked successfully", "appointment": appointment}


def get_all_appointments():
    return appointments


def get_recent_appointments():
    return list(reversed(appointments))


def delete_appointment(appointment_id: int):
    for index, appointment in enumerate(appointments):
        if appointment.appointment_id == appointment_id:
            deleted_appointment = appointments.pop(index)
            return {"message": "Appointment deleted successfully", "appointment": deleted_appointment}
    return {"message": "Appointment not found"}


def get_patient_appointments(patient_id: int):
    return [
        appointment
        for appointment in appointments
        if appointment.patient_id == patient_id
    ]
