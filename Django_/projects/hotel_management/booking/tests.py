from django.test import TestCase
from .models import Room, Reservation
from datetime import date


class BookingModelsTest(TestCase):
    def test_room_creation(self):
        room = Room.objects.create(room_number='101', room_type='single', price=100.00)
        self.assertEqual(str(room), 'Room 101 (Single)')

    def test_reservation_creation(self):
        room = Room.objects.create(room_number='101', room_type='single', price=100.00)
        reservation = Reservation.objects.create(
            guest_name='Alice',
            guest_email='alice@example.com',
            room=room,
            check_in=date(2026, 7, 1),
            check_out=date(2026, 7, 4),
        )
        self.assertEqual(str(reservation), 'Alice - Room 101 (Single)')
