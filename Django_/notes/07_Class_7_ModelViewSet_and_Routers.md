# Class 7: ModelViewSet and Routers

## Learning Objectives

After this class, you will understand:

- What `ModelViewSet` is
- How routers simplify API URLs
- How to build CRUD APIs with DRF

## What is `ModelViewSet`?

`ModelViewSet` is a DRF class that provides full CRUD behavior for a model.
It combines list, create, retrieve, update, and delete actions.

Example:

```python
from rest_framework import viewsets
from .models import Room
from .serializers import RoomSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
```

## What are Routers?

Routers generate URL patterns for viewsets automatically.
They make API routing cleaner.

Example:

```python
from rest_framework.routers import DefaultRouter
from .api import RoomViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)

urlpatterns = router.urls
```

## CRUD APIs with DRF

With `ModelViewSet`, you get:

- `GET /rooms/` — list rooms
- `POST /rooms/` — create a room
- `GET /rooms/{id}/` — retrieve a room
- `PUT /rooms/{id}/` — update a room
- `DELETE /rooms/{id}/` — delete a room

## Summary

This class covered:

- ModelViewSet
- routers
- CRUD APIs in DRF

## Interview Questions

1. What is `ModelViewSet`?
2. How do routers simplify API URLs?
3. What endpoints does a viewset provide?

## Exercises

1. Create a `RoomViewSet` for the `Room` model.
2. Register it with a router.
3. Test the API in the browser or Postman.
