"""
Appointment Router

REST API endpoints for appointment management.
"""

from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.appointment import Appointment, AppointmentCreate, AppointmentUpdate
import app.services.appointment_service as appointment_service


router = APIRouter(prefix="/appointments", tags=["Appointments"])


@router.get("", response_model=List[dict])
async def get_all_appointments():
    """Get all appointments."""
    return appointment_service.get_all_appointments()


@router.get("/{appointment_id}", response_model=dict)
async def get_appointment(appointment_id: int):
    """Get a specific appointment by ID."""
    # Find the appointment using the service
    appointment = appointment_service.find_appointment_by_id(appointment_id)
    
    # If not found, raise error
    if appointment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Appointment with ID {appointment_id} not found"
        )
    
    # Return as dictionary
    return appointment.to_dict()


@router.get("/patient/{patient_id}", response_model=List[dict])
async def get_appointments_by_patient(patient_id: int):
    """Get all appointments for a patient."""
    return appointment_service.find_appointments_by_patient(patient_id)


@router.get("/doctor/{doctor_id}", response_model=List[dict])
async def get_appointments_by_doctor(doctor_id: int):
    """Get all appointments for a doctor."""
    return appointment_service.find_appointments_by_doctor(doctor_id)


@router.get("/search/available/{status}", response_model=List[dict])
async def get_appointments_by_status(status: str):
    """Get appointments by status."""
    return appointment_service.find_available_appointments(status)


@router.post("", response_model=dict, status_code=status.HTTP_201_CREATED)
async def book_appointment(appointment_create: AppointmentCreate):
    """Book a new appointment."""
    # Call service to create appointment
    return appointment_service.create_appointment(
        patient_id=appointment_create.patient_id,
        doctor_id=appointment_create.doctor_id,
        appointment_date=appointment_create.appointment_date
    )


@router.put("/{appointment_id}", response_model=dict)
async def update_appointment(appointment_id: int, appointment_update: AppointmentUpdate):
    """Update an appointment."""
    # Validate ID
    if appointment_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Appointment ID must be positive"
        )
    
    # Check if appointment exists
    appointment = appointment_service.find_appointment_by_id(appointment_id)
    if appointment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Appointment with ID {appointment_id} not found"
        )
    
    # Call patch service since we want partial update
    return appointment_service.patch_appointment(
        appointment_id=appointment_id,
        patient_id=appointment_update.patient_id if hasattr(appointment_update, 'patient_id') and appointment_update.patient_id else None,
        doctor_id=appointment_update.doctor_id if hasattr(appointment_update, 'doctor_id') and appointment_update.doctor_id else None,
        appointment_date=appointment_update.appointment_date,
        status=appointment_update.status
    )


@router.delete("/{appointment_id}", status_code=status.HTTP_200_OK)
async def cancel_appointment(appointment_id: int):
    """Cancel an appointment."""
    # Validate ID
    if appointment_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Appointment ID must be positive"
        )
    
    # Cancel the appointment
    deleted = appointment_service.delete_appointment(appointment_id)
    
    # If not found, raise error
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Appointment with ID {appointment_id} not found"
        )
    
    return {"message": f"Appointment {appointment_id} has been cancelled"}
