# Class 6: Django REST Framework (DRF)

## 1. What is DRF?
- Django REST Framework is used to build APIs.
- It helps return JSON responses for frontend or mobile apps.

## 2. Why use DRF?
- Easy API creation
- Built-in serializers
- Authentication support
- Browsable API interface

## 3. Install DRF
- Add to `requirements.txt`:
  - `djangorestframework==3.15.2`
- Install:
  - `pip install -r requirements.txt`

## 4. Add DRF to Installed Apps
In `config/settings.py`:
- `'rest_framework'`

## 5. Serializer
A serializer converts model data to JSON and also validates incoming data.

Example in `students/serializers.py`:
- `StudentSerializer`

## 6. APIView
- `APIView` is used for custom API logic.
- A class-based view handles GET, POST, PUT, DELETE methods.

## 7. Response and Status Codes
- Use `Response` from DRF
- Common status codes:
  - `200 OK`
  - `201 Created`
  - `204 No Content`
  - `400 Bad Request`
  - `404 Not Found`
