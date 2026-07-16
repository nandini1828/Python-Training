"""
Doctor Tests

Test cases for doctor-related functionality.
"""

import pytest
from app.models.doctor import Doctor, DoctorUpdate
from app.services.doctor_service import DoctorService, doctors


class TestDoctorService:
    """
    Test class for Doctor Service.
    """
    
    def setup_method(self):
        """
        Setup method to initialize fresh test data before each test.
        
        This ensures each test starts with the same state.
        """
        doctors.clear()
        doctors.append(Doctor(id=1, name="Dr. Smith", specialization="Cardiology", experience=10))
        doctors.append(Doctor(id=2, name="Dr. Johnson", specialization="Neurology", experience=8))
    
    def test_get_all_doctors(self):
        """
        Test retrieving all doctors.
        """
        result = DoctorService.get_all_doctors()
        
        assert isinstance(result, list)
        assert len(result) == 2
    
    def test_get_doctor_by_id_found(self):
        """
        Test retrieving an existing doctor by ID.
        """
        result = DoctorService.get_doctor_by_id(1)
        
        assert result is not None
        assert result.id == 1
        assert result.name == "Dr. Smith"
        assert result.specialization == "Cardiology"
    
    def test_get_doctor_by_id_not_found(self):
        """
        Test retrieving a non-existent doctor.
        """
        result = DoctorService.get_doctor_by_id(999)
        
        assert result is None
    
    def test_add_doctor(self):
        """
        Test adding a new doctor.
        """
        new_doctor = Doctor(id=3, name="Dr. Williams", specialization="Orthopedics", experience=12)
        
        result = DoctorService.add_doctor(new_doctor)
        
        assert result.id == 3
        assert result.name == "Dr. Williams"
        assert len(doctors) == 3
    
    def test_update_doctor_found(self):
        """
        Test updating a doctor's specialization.
        """
        update = DoctorUpdate(specialization="Pediatrics")
        
        result = DoctorService.update_doctor(1, update)
        
        assert result is not None
        assert result.specialization == "Pediatrics"
        # Other fields should remain unchanged
        assert result.name == "Dr. Smith"
    
    def test_update_doctor_not_found(self):
        """
        Test updating a non-existent doctor.
        """
        update = DoctorUpdate(specialization="Psychiatry")
        
        result = DoctorService.update_doctor(999, update)
        
        assert result is None
    
    def test_delete_doctor_found(self):
        """
        Test deleting an existing doctor.
        """
        assert len(doctors) == 2
        
        result = DoctorService.delete_doctor(1)
        
        assert result is True
        assert len(doctors) == 1
        assert DoctorService.get_doctor_by_id(1) is None
    
    def test_delete_doctor_not_found(self):
        """
        Test deleting a non-existent doctor.
        """
        result = DoctorService.delete_doctor(999)
        
        assert result is False
        assert len(doctors) == 2
