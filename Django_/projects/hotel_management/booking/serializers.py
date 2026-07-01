from rest_framework import serializers
from .models import Guest, Room, Reservation


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'name', 'email', 'phone']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'price', 'is_available']


class ReservationSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Room.objects.all(),
        source='room'
    )
    guest = GuestSerializer(read_only=True)
    guest_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Guest.objects.all(),
        source='guest'
    )

    class Meta:
        model = Reservation
        fields = [
            'id',
            'guest',
            'guest_id',
            'room',
            'room_id',
            'check_in',
            'check_out',
            'status',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at', 'guest', 'room']
