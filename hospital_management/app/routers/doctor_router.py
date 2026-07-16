"""
Doctor Router

REST API endpoints for doctor management.
"""

from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.doctor import Doctor, DoctorUpdate
import app.services.doctor_service as doctor_service


router = APIRouter(prefix="/doctors", tags=["Doctors"])


@router.get("", response_model=List[dict])
async def get_all_doctors():
    """Get all doctors."""
    return doctor_service.get_all_doctors()


@router.get("/{doctor_id}", response_model=dict)
async def get_doctor(doctor_id: int):
    """Get a specific doctor by ID."""
    # Find the doctor using the service
    doctor = doctor_service.find_doctor_by_id(doctor_id)
    
    # If not found, raise error
    if doctor is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Doctor with ID {doctor_id} not found"
        )
    
    # Return as dictionary
    return doctor.to_dict()


@router.get("/search/by-name/{name}", response_model=List[dict])
async def search_doctors_by_name(name: str):
    """Search doctors by name."""
    return doctor_service.find_doctors_by_name(name)


@router.get("/search/by-specialization/{specialization}", response_model=List[dict])
async def search_doctors_by_specialization(specialization: str):
    """Search doctors by specialization."""
    return doctor_service.find_doctors_by_specialization(specialization)


@router.post("", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_doctor(doctor: Doctor):
    """Create a new doctor."""
    # Call service to create doctor
    return doctor_service.create_doctor(
        name=doctor.name,
        specialization=doctor.specialization,
        experience=doctor.experience
    )


@router.put("/{doctor_id}", response_model=dict)
async def update_doctor(doctor_id: int, doctor_update: DoctorUpdate):
    """Update a doctor's information."""
    # Validate ID
    if doctor_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Doctor ID must be positive"
        )
    
    # Check if doctor exists
    doctor = doctor_service.find_doctor_by_id(doctor_id)
    if doctor is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Doctor with ID {doctor_id} not found"
        )
    
    # Call patch service since we want partial update
    return doctor_service.patch_doctor(
        doctor_id=doctor_id,
        name=doctor_update.name,
        specialization=doctor_update.specialization,
        experience=doctor_update.experience
    )


@router.delete("/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_doctor(doctor_id: int):
    """Delete a doctor."""
    # Validate ID
    if doctor_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Doctor ID must be positive"
        )
    
    # Delete the doctor
    deleted = doctor_service.delete_doctor(doctor_id)
    
    # If not found, raise error
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Doctor with ID {doctor_id} not found"
        )
