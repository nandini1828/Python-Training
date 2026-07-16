"""
Appointment Service

This service contains business logic for managing appointments.
Static in-memory data is stored here.
"""

from typing import Optional, List
from datetime import datetime
from app.models.appointment import Appointment, AppointmentCreate, AppointmentUpdate


# Static data - list of appointments stored in memory
appointments: List[Appointment] = [
    Appointment(
        id=1,
        patient_id=1,
        doctor_id=1,
        appointment_date=datetime(2024, 12, 20, 10, 0),
        status="Scheduled"
    ),
    Appointment(
        id=2,
        patient_id=2,
        doctor_id=2,
        appointment_date=datetime(2024, 12, 21, 14, 30),
        status="Scheduled"
    ),
]


def get_all_appointments() -> List[dict]:
    """
    Get all appointments.
    
    Returns:
        List of appointment dictionaries.
    """
    result = []
    for appointment in appointments:
        result.append(appointment.to_dict())
    return result


def find_appointment_by_id(appointment_id: int) -> Optional[Appointment]:
    """
    Find an appointment by ID.
    
    Args:
        appointment_id: The ID to search for.
        
    Returns:
        Appointment object if found, None otherwise.
    """
    # Loop through all appointments
    for appointment in appointments:
        # Check if this appointment's ID matches
        if appointment.id == appointment_id:
            return appointment
    
    # If not found, return None
    return None


def find_appointments_by_patient(patient_id: int) -> List[dict]:
    """
    Find all appointments for a patient.
    
    Args:
        patient_id: The patient ID to search for.
        
    Returns:
        List of appointment dictionaries.
    """
    result = []
    
    # Loop through all appointments
    for appointment in appointments:
        # Check if this appointment belongs to the patient
        if appointment.patient_id == patient_id:
            result.append(appointment.to_dict())
    
    return result


def find_appointments_by_doctor(doctor_id: int) -> List[dict]:
    """
    Find all appointments for a doctor.
    
    Args:
        doctor_id: The doctor ID to search for.
        
    Returns:
        List of appointment dictionaries.
    """
    result = []
    
    # Loop through all appointments
    for appointment in appointments:
        # Check if this appointment belongs to the doctor
        if appointment.doctor_id == doctor_id:
            result.append(appointment.to_dict())
    
    return result


def find_available_appointments(status: str = "Scheduled") -> List[dict]:
    """
    Find appointments by status.
    
    Args:
        status: The status to search for.
        
    Returns:
        List of appointment dictionaries.
    """
    result = []
    
    # Loop through all appointments
    for appointment in appointments:
        # Check if appointment has the given status
        if appointment.status == status:
            result.append(appointment.to_dict())
    
    return result


def create_appointment(patient_id: int, doctor_id: int, appointment_date: datetime) -> dict:
    """
    Create a new appointment.
    
    Args:
        patient_id: The patient ID.
        doctor_id: The doctor ID.
        appointment_date: The appointment date and time.
        
    Returns:
        Created appointment as dictionary.
    """
    # Find the highest ID
    highest_id = 0
    for appointment in appointments:
        if appointment.id > highest_id:
            highest_id = appointment.id
    
    # Create new appointment with new ID
    new_appointment = Appointment(
        id=highest_id + 1,
        patient_id=patient_id,
        doctor_id=doctor_id,
        appointment_date=appointment_date,
        status="Scheduled"
    )
    
    # Add to list
    appointments.append(new_appointment)
    
    # Return as dictionary
    return new_appointment.to_dict()


def update_appointment(appointment_id: int, patient_id: int, doctor_id: int, appointment_date: datetime, status: str) -> Optional[dict]:
    """
    Update an appointment's information.
    
    Args:
        appointment_id: ID of appointment to update.
        patient_id: New patient ID.
        doctor_id: New doctor ID.
        appointment_date: New appointment date.
        status: New status.
        
    Returns:
        Updated appointment as dictionary if found, None otherwise.
    """
    # Find the appointment
    appointment = find_appointment_by_id(appointment_id)
    if appointment is None:
        return None
    
    # Get the index
    appointment_index = appointments.index(appointment)
    
    # Create updated appointment
    updated_appointment = Appointment(
        id=appointment.id,
        patient_id=patient_id,
        doctor_id=doctor_id,
        appointment_date=appointment_date,
        status=status
    )
    
    # Replace in list
    appointments[appointment_index] = updated_appointment
    
    # Return as dictionary
    return updated_appointment.to_dict()


def patch_appointment(appointment_id: int, patient_id: int = None, doctor_id: int = None, appointment_date: datetime = None, status: str = None) -> Optional[dict]:
    """
    Partially update an appointment's information.
    
    Args:
        appointment_id: ID of appointment to update.
        patient_id: New patient ID (optional).
        doctor_id: New doctor ID (optional).
        appointment_date: New appointment date (optional).
        status: New status (optional).
        
    Returns:
        Updated appointment as dictionary if found, None otherwise.
    """
    # Find the appointment
    appointment = find_appointment_by_id(appointment_id)
    if appointment is None:
        return None
    
    # Get the index
    appointment_index = appointments.index(appointment)
    
    # Get existing values, replace only if provided
    new_patient_id = patient_id if patient_id is not None else appointment.patient_id
    new_doctor_id = doctor_id if doctor_id is not None else appointment.doctor_id
    new_appointment_date = appointment_date if appointment_date is not None else appointment.appointment_date
    new_status = status if status is not None else appointment.status
    
    # Create updated appointment
    updated_appointment = Appointment(
        id=appointment.id,
        patient_id=new_patient_id,
        doctor_id=new_doctor_id,
        appointment_date=new_appointment_date,
        status=new_status
    )
    
    # Replace in list
    appointments[appointment_index] = updated_appointment
    
    # Return as dictionary
    return updated_appointment.to_dict()


def delete_appointment(appointment_id: int) -> bool:
    """
    Delete an appointment from the system.
    
    Args:
        appointment_id: ID of appointment to delete.
        
    Returns:
        True if deleted, False if not found.
    """
    # Find the appointment
    appointment = find_appointment_by_id(appointment_id)
    if appointment is None:
        return False
    
    # Remove the appointment from the list
    appointments.remove(appointment)
    
    # Return True to show it was deleted
    return True
