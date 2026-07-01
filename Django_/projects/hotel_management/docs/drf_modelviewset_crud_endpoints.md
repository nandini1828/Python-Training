# Django REST Framework CRUD APIs with ModelViewSet

This document explains how this project implements CRUD APIs for its models using Django REST Framework's `ModelViewSet` and router registration.

## DRF ModelViewSet Overview

A `ModelViewSet` is a DRF class that provides all standard CRUD operations for a model in a single class:

- `list()` → GET collection
- `retrieve()` → GET single record
- `create()` → POST new record
- `update()` → PUT existing record
- `partial_update()` → PATCH existing record
- `destroy()` → DELETE record

In this project, `ModelViewSet` is implemented in `booking/api.py`.

## API viewsets in `booking/api.py`

File: `booking/api.py`

```python
from rest_framework import viewsets
from .models import Guest, Room, Reservation
from .serializers import GuestSerializer, RoomSerializer, ReservationSerializer


class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
```

Each viewset defines:

- `queryset`: the records exposed by the API
- `serializer_class`: the serializer used to validate input and format output

With this setup, the viewsets automatically provide full CRUD support for the `Guest`, `Room`, and `Reservation` models.

## URL routing with DRF router

File: `booking/urls.py`

The `DefaultRouter` attaches the viewsets to standard REST URL patterns:

```python
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .api import GuestViewSet, RoomViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'guests', GuestViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('reservation-confirmation/<int:reservation_id>/', views.reservation_confirmation, name='reservation_confirmation'),
    path('manage/', views.manage_reservations, name='manage_reservations'),
    path('manage/<int:reservation_id>/<str:action>/', views.manage_reservation_action, name='manage_reservation_action'),
    path('api/', include(router.urls)),
]
```

The router creates these endpoints by default:

- `GET /api/guests/`
- `POST /api/guests/`
- `GET /api/guests/{id}/`
- `PUT /api/guests/{id}/`
- `PATCH /api/guests/{id}/`
- `DELETE /api/guests/{id}/`
- `GET /api/rooms/`
- `POST /api/rooms/`
- `GET /api/rooms/{id}/`
- `PUT /api/rooms/{id}/`
- `PATCH /api/rooms/{id}/`
- `DELETE /api/rooms/{id}/`
- `GET /api/reservations/`
- `POST /api/reservations/`
- `GET /api/reservations/{id}/`
- `PUT /api/reservations/{id}/`
- `PATCH /api/reservations/{id}/`
- `DELETE /api/reservations/{id}/`

## Example CRUD usage

### Create a guest

POST `/api/guests/`

Request body:

```json
{
  "name": "Alice Smith",
  "email": "alice@example.com",
  "phone": "+1234567890"
}
```

### Update a room

PATCH `/api/rooms/5/`

Request body:

```json
{
  "price": "199.99",
  "is_available": false
}
```

### Create a reservation

POST `/api/reservations/`

Request body:

```json
{
  "guest_id": 1,
  "room_id": 2,
  "check_in": "2026-07-10",
  "check_out": "2026-07-14"
}
```

## Notes on the reservation serializer

The reservation API uses nested read-only objects with write-only IDs, so responses include full `guest` and `room` objects while requests only need IDs.

This keeps response data rich and request payloads simple.

## Summary

- CRUD APIs are implemented using DRF `ModelViewSet` classes in `booking/api.py`.
- The router in `booking/urls.py` exposes API endpoints under `/api/`.
- `Guest`, `Room`, and `Reservation` are all available for standard create, list, retrieve, update, and delete operations.
