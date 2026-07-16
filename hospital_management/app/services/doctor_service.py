"""
Doctor Service

This service contains business logic for managing doctors.
Static in-memory data is stored here.
"""

from typing import Optional, List
from app.models.doctor import Doctor, DoctorUpdate


# Static data - list of doctors stored in memory
doctors: List[Doctor] = [
    Doctor(id=1, name="Dr. Smith", specialization="Cardiology", experience=10),
    Doctor(id=2, name="Dr. Johnson", specialization="Neurology", experience=8),
    Doctor(id=3, name="Dr. Williams", specialization="Orthopedics", experience=12),
]


def get_all_doctors() -> List[dict]:
    """
    Get all doctors.
    
    Returns:
        List of doctor dictionaries.
    """
    result = []
    for doctor in doctors:
        result.append(doctor.to_dict())
    return result


def find_doctor_by_id(doctor_id: int) -> Optional[Doctor]:
    """
    Find a doctor by their ID.
    
    Args:
        doctor_id: The ID to search for.
        
    Returns:
        Doctor object if found, None otherwise.
    """
    # Loop through all doctors
    for doctor in doctors:
        # Check if this doctor's ID matches
        if doctor.id == doctor_id:
            return doctor
    
    # If not found, return None
    return None


def find_doctors_by_name(name: str) -> List[dict]:
    """
    Find doctors by name (partial match).
    
    Args:
        name: The name to search for.
        
    Returns:
        List of doctor dictionaries.
    """
    result = []
    
    # Loop through all doctors
    for doctor in doctors:
        # Check if name is contained in doctor's name
        if name.lower() in doctor.name.lower():
            result.append(doctor.to_dict())
    
    return result


def find_doctors_by_specialization(specialization: str) -> List[dict]:
    """
    Find doctors by specialization.
    
    Args:
        specialization: The specialization to search for.
        
    Returns:
        List of doctor dictionaries.
    """
    result = []
    
    # Loop through all doctors
    for doctor in doctors:
        # Check if specialization matches (case-insensitive)
        if specialization.lower() == doctor.specialization.lower():
            result.append(doctor.to_dict())
    
    return result


def create_doctor(name: str, specialization: str, experience: int) -> dict:
    """
    Create a new doctor.
    
    Args:
        name: Doctor's name.
        specialization: Doctor's specialization.
        experience: Years of experience.
        
    Returns:
        Created doctor as dictionary.
    """
    # Find the highest ID
    highest_id = 0
    for doctor in doctors:
        if doctor.id > highest_id:
            highest_id = doctor.id
    
    # Create new doctor with new ID
    new_doctor = Doctor(
        id=highest_id + 1,
        name=name,
        specialization=specialization,
        experience=experience
    )
    
    # Add to list
    doctors.append(new_doctor)
    
    # Return as dictionary
    return new_doctor.to_dict()


def update_doctor(doctor_id: int, name: str, specialization: str, experience: int) -> Optional[dict]:
    """
    Update a doctor's information.
    
    Args:
        doctor_id: ID of doctor to update.
        name: New name.
        specialization: New specialization.
        experience: New experience.
        
    Returns:
        Updated doctor as dictionary if found, None otherwise.
    """
    # Find the doctor
    doctor = find_doctor_by_id(doctor_id)
    if doctor is None:
        return None
    
    # Get the index
    doctor_index = doctors.index(doctor)
    
    # Create updated doctor
    updated_doctor = Doctor(
        id=doctor.id,
        name=name,
        specialization=specialization,
        experience=experience
    )
    
    # Replace in list
    doctors[doctor_index] = updated_doctor
    
    # Return as dictionary
    return updated_doctor.to_dict()


def patch_doctor(doctor_id: int, name: str = None, specialization: str = None, experience: int = None) -> Optional[dict]:
    """
    Partially update a doctor's information.
    
    Args:
        doctor_id: ID of doctor to update.
        name: New name (optional).
        specialization: New specialization (optional).
        experience: New experience (optional).
        
    Returns:
        Updated doctor as dictionary if found, None otherwise.
    """
    # Find the doctor
    doctor = find_doctor_by_id(doctor_id)
    if doctor is None:
        return None
    
    # Get the index
    doctor_index = doctors.index(doctor)
    
    # Get existing values, replace only if provided
    new_name = name if name is not None else doctor.name
    new_specialization = specialization if specialization is not None else doctor.specialization
    new_experience = experience if experience is not None else doctor.experience
    
    # Create updated doctor
    updated_doctor = Doctor(
        id=doctor.id,
        name=new_name,
        specialization=new_specialization,
        experience=new_experience
    )
    
    # Replace in list
    doctors[doctor_index] = updated_doctor
    
    # Return as dictionary
    return updated_doctor.to_dict()


def delete_doctor(doctor_id: int) -> bool:
    """
    Delete a doctor from the system.
    
    Args:
        doctor_id: ID of doctor to delete.
        
    Returns:
        True if deleted, False if not found.
    """
    # Find the doctor
    doctor = find_doctor_by_id(doctor_id)
    if doctor is None:
        return False
    
    # Remove the doctor from the list
    doctors.remove(doctor)
    
    # Return True to show it was deleted
    return True
