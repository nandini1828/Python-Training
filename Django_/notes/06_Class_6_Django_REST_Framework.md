# Class 6: Django REST Framework

## Learning Objectives

After this class, you will understand:

- What Django REST Framework (DRF) is
- Why DRF is used for APIs
- What `APIView` is
- What serializers do
- How responses and status codes work

## What is Django REST Framework?

Django REST Framework is a toolkit for building web APIs with Django.
It makes API development easier and more maintainable.

DRF provides:

- serializers
- view classes
- authentication
- permissions
- browsable API

## What is `APIView`?

`APIView` is a DRF view class for handling API requests.
It is similar to Django views but designed for APIs.

Example:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RoomList(APIView):
    def get(self, request):
        return Response({'message': 'Hello'}, status=status.HTTP_200_OK)
```

## What is a Serializer?

Serializers convert model instances to JSON and validate input data.
They are similar to Django forms.

Example:

```python
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
```

## Response and Status Codes

DRF uses `Response` objects instead of `HttpResponse`.

Example:

```python
return Response(data, status=status.HTTP_200_OK)
```

Common status codes:

- `200 OK`
- `201 Created`
- `400 Bad Request`
- `401 Unauthorized`
- `404 Not Found`
- `500 Internal Server Error`

## Summary

This class covered:

- DRF basics
- APIView
- serializers
- Response
- status codes

## Interview Questions

1. What is Django REST Framework?
2. What is `APIView`?
3. What is a serializer?
4. Why do APIs use status codes?

## Exercises

1. Install DRF in the project requirements.
2. Add `rest_framework` to `INSTALLED_APPS`.
3. Create a serializer for the `Room` model.
