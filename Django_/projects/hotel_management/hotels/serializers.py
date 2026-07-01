from rest_framework import serializers
from .models import Amenity, Branch, Hotel, Room, RoomType


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['id', 'code', 'name', 'description']


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['id', 'code', 'name', 'description', 'max_guests', 'base_price']


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'code', 'address', 'city', 'country', 'phone', 'email']


class BranchSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)
    hotel_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Hotel.objects.all(), source='hotel')

    class Meta:
        model = Branch
        fields = ['id', 'hotel', 'hotel_id', 'name', 'floor_count', 'address']


class RoomSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)
    branch_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Branch.objects.all(), source='branch')
    room_type = RoomTypeSerializer(read_only=True)
    room_type_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=RoomType.objects.all(), source='room_type')
    amenities = AmenitySerializer(many=True, read_only=True)
    amenity_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Amenity.objects.all(), source='amenities')

    class Meta:
        model = Room
        fields = [
            'id',
            'branch',
            'branch_id',
            'room_number',
            'room_type',
            'room_type_id',
            'amenities',
            'amenity_ids',
            'is_available',
            'price',
        ]
