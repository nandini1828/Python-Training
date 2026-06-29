# Class 7: ModelViewSet and Routers

## 1. ModelViewSet
- `ModelViewSet` provides CRUD operations automatically.
- It is faster than writing each API view manually.

## 2. Router
- A router automatically creates URLs for CRUD endpoints.
- Example:
  - `router.register(r'api/v2/students', StudentViewSet)`

## 3. What we implemented
- `StudentViewSet` in `students/viewsets.py`
- `DefaultRouter` in `students/urls.py`
- Endpoints created automatically:
  - `GET /api/v2/students/`
  - `POST /api/v2/students/`
  - `GET /api/v2/students/<id>/`
  - `PUT /api/v2/students/<id>/`
  - `DELETE /api/v2/students/<id>/`

## 4. Why this is useful
- Saves time
- Clean code
- Great for REST APIs

## 5. Example API Response
```json
[
  {
    "id": 1,
    "first_name": "Aisha",
    "last_name": "Khan",
    "age": 20,
    "email": "aisha@example.com",
    "course": "Django"
  }
]
```
