# Models and Serializers in the Hotel Management Project

This document explains how the main data models are defined in `booking/models.py` and how they are exposed using serializers in `booking/serializers.py`.

## 1. Guest model

File: `booking/models.py`

The `Guest` model captures a hotel guest's contact details:

- `name`: `CharField(max_length=100)`
- `email`: `EmailField(unique=True)`
- `phone`: `CharField(max_length=20, blank=True)`

The guest record is used when someone makes a reservation. The model has a simple `__str__` method so the admin and debug output are readable.

### API exposure

The corresponding serializer is `GuestSerializer` in `booking/serializers.py`:

```python
class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'name', 'email', 'phone']
```

This serializer is a direct `ModelSerializer` mapping fields from the `Guest` model into JSON.

## 2. Room model

File: `booking/models.py`

The `Room` model stores room inventory and availability:

- `room_number`: `CharField(max_length=10, unique=True)`
- `room_type`: `CharField(max_length=20, choices=ROOM_TYPES)`
- `price`: `DecimalField(max_digits=8, decimal_places=2)`
- `is_available`: `BooleanField(default=True)`
- `image_url`: `CharField(max_length=250, default='booking/images/room-default.svg')`

`ROOM_TYPES` defines the allowed room type values (`single`, `double`, `suite`). Rooms are marked available or unavailable so the frontend can display only open inventory.

### API exposure

The room serializer is `RoomSerializer`:

```python
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'price', 'is_available']
```

This allows API clients to read and write room records in the same shape as the model.

## 3. Reservation model

File: `booking/models.py`

The `Reservation` model links a guest and a room and captures booking dates:

- `guest`: `ForeignKey(Guest, on_delete=models.CASCADE, related_name='reservations')`
- `room`: `ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')`
- `check_in`: `DateField()`
- `check_out`: `DateField()`
- `status`: `CharField(max_length=20, choices=RESERVATION_STATUS, default='pending')`
- `created_at`: `DateTimeField(auto_now_add=True)`

`RESERVATION_STATUS` supports workflow states such as `pending`, `approved`, `rejected`, `checked_in`, `checked_out`, and `cancelled`.

### API exposure

The reservation serializer is more advanced because it handles nested read-only objects and write-only foreign key IDs:

```python
class ReservationSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Room.objects.all(), source='room')
    guest = GuestSerializer(read_only=True)
    guest_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Guest.objects.all(), source='guest')

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
```

This serializer exposes nested guest and room data when reading reservations, while allowing clients to create or update a reservation by providing `guest_id` and `room_id`.

## Summary

- `Guest` and `Room` are simple model serializers that map directly to model fields.
- `Reservation` uses nested serializers for readable API output and write-only related fields for creation.
- These serializers are used by the DRF viewsets to implement CRUD APIs for the hotel system.
