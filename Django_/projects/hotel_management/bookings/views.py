from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from booking.models import Guest, Reservation
from booking.serializers import GuestSerializer, ReservationSerializer
from core.permissions import IsAdminOrReadOnly, IsReceptionistOrAdmin, IsReservationOwnerOrStaff


class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [IsAuthenticated, IsReceptionistOrAdmin]


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.select_related('guest', 'room').all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated, IsReservationOwnerOrStaff]
