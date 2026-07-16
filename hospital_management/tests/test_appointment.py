"""
Appointment Tests

Test cases for appointment-related functionality.
"""

import pytest
from datetime import datetime
from app.models.appointment import Appointment, AppointmentCreate, AppointmentUpdate
from app.services.appointment_service import AppointmentService, appointments


class TestAppointmentService:
    """
    Test class for Appointment Service.
    """
    
    def setup_method(self):
        """
        Setup method to initialize fresh test data.
        """
        appointments.clear()
        appointments.append(Appointment(
            id=1,
            patient_id=1,
            doctor_id=1,
            appointment_date=datetime(2024, 12, 20, 10, 0),
            status="Scheduled"
        ))
        appointments.append(Appointment(
            id=2,
            patient_id=2,
            doctor_id=2,
            appointment_date=datetime(2024, 12, 21, 14, 30),
            status="Scheduled"
        ))
    
    def test_get_all_appointments(self):
        """
        Test retrieving all appointments.
        """
        result = AppointmentService.get_all_appointments()
        
        assert isinstance(result, list)
        assert len(result) == 2
    
    def test_get_appointment_by_id_found(self):
        """
        Test retrieving an existing appointment.
        """
        result = AppointmentService.get_appointment_by_id(1)
        
        assert result is not None
        assert result.id == 1
        assert result.patient_id == 1
        assert result.doctor_id == 1
    
    def test_get_appointment_by_id_not_found(self):
        """
        Test retrieving a non-existent appointment.
        """
        result = AppointmentService.get_appointment_by_id(999)
        
        assert result is None
    
    def test_book_appointment(self):
        """
        Test booking a new appointment.
        
        This test demonstrates:
        - Creating an AppointmentCreate object
        - Checking that a new ID is generated
        - Verifying the appointment is added to the list
        """
        appointment_create = AppointmentCreate(
            patient_id=3,
            doctor_id=1,
            appointment_date=datetime(2024, 12, 22, 15, 0)
        )
        
        result = AppointmentService.book_appointment(appointment_create)
        
        # Assert that the appointment was created with a new ID
        assert result.id == 3  # Should be 3 (highest existing ID + 1)
        assert result.patient_id == 3
        assert result.status == "Scheduled"
        
        # Assert that the appointment was added to the list
        assert len(appointments) == 3
    
    def test_get_appointments_by_patient(self):
        """
        Test retrieving all appointments for a specific patient.
        
        This demonstrates list comprehension in the service layer.
        """
        # Get appointments for patient 1
        result = AppointmentService.get_appointments_by_patient(1)
        
        # Assert that we got the correct appointments
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0].patient_id == 1
    
    def test_get_appointments_by_doctor(self):
        """
        Test retrieving all appointments for a specific doctor.
        """
        result = AppointmentService.get_appointments_by_doctor(2)
        
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0].doctor_id == 2
    
    def test_get_appointments_by_patient_none(self):
        """
        Test retrieving appointments for a patient with no appointments.
        """
        result = AppointmentService.get_appointments_by_patient(999)
        
        # Should return an empty list, not None
        assert isinstance(result, list)
        assert len(result) == 0
    
    def test_update_status(self):
        """
        Test updating an appointment's status.
        """
        update = AppointmentUpdate(status="Completed")
        
        result = AppointmentService.update_status(1, update)
        
        assert result is not None
        assert result.status == "Completed"
        # Other fields should remain unchanged
        assert result.patient_id == 1
    
    def test_update_status_not_found(self):
        """
        Test updating status of a non-existent appointment.
        """
        update = AppointmentUpdate(status="Cancelled")
        
        result = AppointmentService.update_status(999, update)
        
        assert result is None
    
    def test_cancel_appointment(self):
        """
        Test cancelling an appointment.
        
        This is a convenience method that updates status to "Cancelled".
        """
        result = AppointmentService.cancel_appointment(1)
        
        # Assert that cancellation was successful
        assert result is True
        
        # Assert that the status was updated
        appointment = AppointmentService.get_appointment_by_id(1)
        assert appointment is not None
        assert appointment.status == "Cancelled"
    
    def test_cancel_appointment_not_found(self):
        """
        Test cancelling a non-existent appointment.
        """
        result = AppointmentService.cancel_appointment(999)
        
        assert result is False
