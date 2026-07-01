# Hotel Management Project Overview

This file is a single authoritative overview of the Hotel Management Django project. It explains the architecture, apps, authentication, permissions, deployment, database setup, and how to run the system.

## Project purpose

This project is an enterprise-style hotel booking backend built with Django and Django REST Framework. It supports:
- Role-based enterprise users
- Hotel inventory and room management
- Guest and reservation workflows
- JWT-secured API access
- Swagger/OpenAPI documentation
- Docker and PostgreSQL support
- Legacy booking pages for session-based users

## Core apps and responsibilities

### `users`
- Custom `User` model in `users/models.py`
- Enterprise profile fields: `department`, `role`, `is_employee`
- Role choices: `admin`, `manager`, `receptionist`, `housekeeping`, `maintenance`, `guest`
- Admin registration in `users/admin.py`
- API viewset in `users/views.py`
- Serializer in `users/serializers.py`

### `hotels`
- Hotel catalog models in `hotels/models.py`
- Includes `Hotel`, `Branch`, `RoomType`, `Amenity`, `Room`
- API viewsets in `hotels/views.py`
- CRUD endpoints for hotel inventory management

### `bookings`
- API app for enterprise booking resources
- Models come from legacy `booking` app and are exposed via API
- Viewsets in `bookings/views.py`
- Endpoints for `guests` and `reservations`

### `booking`
- Legacy frontend app with templates for guest booking pages
- Contains `booking/models.py`, `booking/views.py`, `booking/urls.py`
- Provides the user-facing booking experience at `/`

### `core`
- Shared logic and permission classes in `core/permissions.py`
- Central place for enterprise access rules

## Authentication and security

### JWT authentication
- Configured in `config/settings.py`
- Uses `rest_framework_simplejwt.authentication.JWTAuthentication`
- Token endpoints in `config/auth_urls.py`
- Exposed at:
  - `POST /api/auth/token/`
  - `POST /api/auth/token/refresh/`

### Role-based permissions
- `users.User.role` drives enterprise authorization
- `core/permissions.py` defines:
  - `IsAdminOrReadOnly`
  - `IsManagerOrReadOnly`
  - `IsReceptionistOrAdmin`
  - `IsReservationOwnerOrStaff`
- These permissions are applied in viewsets to protect hotel, guest, reservation, and user APIs
- Example behavior:
  - `admin` and staff users can fully manage enterprise resources
  - `receptionist` can create and update guests/reservations
  - Default `guest` users have read-only reservation access

## API architecture

### Router and URLs
- `config/routers.py` centralizes DRF routing
- Registered endpoints:
  - `/api/hotels/`
  - `/api/branches/`
  - `/api/room-types/`
  - `/api/amenities/`
  - `/api/rooms/`
  - `/api/guests/`
  - `/api/reservations/`
  - `/api/users/`
- `config/urls.py` also exposes:
  - `/admin/`
  - `/api/schema/`
  - `/api/docs/`
  - `/accounts/login/` and `/accounts/logout/`
  - legacy `booking.urls`

### Documentation
- Swagger UI available at `/api/docs/`
- OpenAPI schema available at `/api/schema/`

## Database and migration strategy

### Database configuration
- Default uses SQLite for local development
- PostgreSQL integration enabled through environment variables
- Database settings in `config/settings.py`
- `.env.example` contains the expected variables:
  - `DJANGO_SECRET_KEY`
  - `DJANGO_DEBUG`
  - `DJANGO_ALLOWED_HOSTS`
  - `DJANGO_DB_ENGINE`
  - `POSTGRES_DB`
  - `POSTGRES_USER`
  - `POSTGRES_PASSWORD`
  - `POSTGRES_HOST`
  - `POSTGRES_PORT`
  - `JWT_ACCESS_LIFETIME_MINUTES`
  - `JWT_REFRESH_TOKEN_DAYS`

### Migration workflow
- Create migrations:
  - `python manage.py makemigrations`
- Apply migrations:
  - `python manage.py migrate`
- Local reset guidance (development only):
  - `python manage.py migrate zero`
  - `python manage.py migrate`

> Warning: Do not use `migrate zero` in production unless you have a verified backup.

## Running the project

### Local development
1. Change into the project root:
   - `cd projects/hotel_management`
2. Activate the virtual environment:
   - `source .venv/bin/activate`
3. Install dependencies if needed:
   - `pip install -r requirements.txt`
4. Run migrations:
   - `python manage.py migrate`
5. Start the server:
   - `python manage.py runserver`
6. Open:
   - `http://127.0.0.1:8000/`

### Docker deployment
1. Create `.env` from `.env.example`
2. Build and run:
   - `docker compose up --build`
3. Apply migrations inside the container:
   - `docker compose run web python manage.py migrate`
4. Create a superuser if needed:
   - `docker compose run web python manage.py createsuperuser`

## Production notes

- Set `DEBUG=False`
- Configure `ALLOWED_HOSTS` correctly
- Use PostgreSQL in production
- Serve static files separately from Django via a web server or CDN
- Keep `AUTH_USER_MODEL` stable once migrations are applied

## Summary of key files

- `config/settings.py` — project settings, auth, database, installed apps
- `config/urls.py` — root URL configuration
- `config/routers.py` — DRF router registration
- `users/models.py` — custom user and enterprise roles
- `users/views.py` — user API endpoints
- `hotels/views.py` — hotel inventory APIs
- `bookings/views.py` — guest and reservation APIs
- `booking/views.py` — legacy booking frontend views
- `core/permissions.py` — shared permission logic
- `docs/project_architecture.md` — architecture explanation
- `README.md` — project setup and basic usage

## What this file covers

This single file unifies the major concepts, architecture, setup, authentication, permissions, database strategy, and deployment steps for the Hotel Management project.
