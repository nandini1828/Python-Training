from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Amenity, Branch, Hotel, RoomType, Room
from .serializers import AmenitySerializer, BranchSerializer, HotelSerializer, RoomSerializer, RoomTypeSerializer
from core.permissions import IsAdminOrReadOnly


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.select_related('branch', 'room_type').prefetch_related('amenities').all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
