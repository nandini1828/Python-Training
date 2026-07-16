"""
appointment_service.py

This module contains all the business logic
related to appointments.
"""

from app.data import appointments, patients, doctors
from app.models.appointment import Appointment
from app.utils import get_next_id, appointment_generator


def book_appointment(
    patient_id: int,
    doctor_id: int,
    appointment_date: str,
):
    """
    Book a new appointment.
    """

    # Check whether patient exists
    if patient_id not in patients:
        return {"message": "Patient not found"}

    # Check whether doctor exists
    if doctor_id not in doctors:
        return {"message": "Doctor not found"}

    # Generate appointment ID
    appointment_id = get_next_id(appointments)

    # Create Appointment object
    appointment = Appointment(
        appointment_id=appointment_id,
        patient_id=patient_id,
        doctor_id=doctor_id,
        appointment_date=appointment_date,
    )

    # Store appointment in list
    appointments.append(appointment)

    return {
        "message": "Appointment booked successfully",
        "appointment": appointment,
    }


def get_all_appointments():
    """
    Return all appointments.
    """

    return appointments


def get_recent_appointments():
    """
    Return appointments in reverse order.

    Demonstrates reversed().
    """

    return list(reversed(appointments))


def delete_appointment(appointment_id: int):
    """
    Delete an appointment.
    """

    # enumerate() gives both index and object
    for index, appointment in enumerate(appointments):

        if appointment.appointment_id == appointment_id:

            deleted_appointment = appointments.pop(index)

            return {
                "message": "Appointment deleted successfully",
                "appointment": deleted_appointment,
            }

    return {"message": "Appointment not found"}


def get_patient_appointments(patient_id: int):
    """
    Return appointments of a specific patient.

    Demonstrates list comprehension.
    """

    return [
        appointment
        for appointment in appointments
        if appointment.patient_id == patient_id
    ]


def display_appointments():
    """
    Display appointments using a generator.

    Demonstrates generators.
    """

    for appointment in appointment_generator(appointments):
        print(appointment)