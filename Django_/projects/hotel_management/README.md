# Hotel Management Django Project

This is a sample Django project for learning how to build a hotel booking system.

## Setup

1. Open a terminal in `projects/hotel_management`.
2. Activate your virtual environment:
   - `source .venv/bin/activate`
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Run migrations:
   - `python manage.py migrate`
5. Start the server:
   - `python manage.py runserver`
6. Open the browser at:
   - `http://127.0.0.1:8000/`

## Docker deployment

1. Copy environment values from `.env.example` to `.env` and customize as needed.
2. Build and start containers:
   - `docker compose up --build`
3. Run migrations inside the container:
   - `docker compose run web python manage.py migrate`
4. Create a superuser inside the container:
   - `docker compose run web python manage.py createsuperuser`
5. Open the browser at:
   - `http://127.0.0.1:8000/`

## Environment variables

Use `.env.example` as a template for the following values:

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

## Project structure

- `config/` — Django project settings and URL configuration
- `booking/` — main application for rooms and reservations
- `manage.py` — Django command utility
- `requirements.txt` — dependencies used by the project

## What this app includes

- Enterprise architecture with separate apps for users, hotels, bookings, and core logic
- Custom `User` model with enterprise profile data and role-based access control
- Hotel inventory models: `Hotel`, `Branch`, `RoomType`, `Amenity`, `Room`
- Booking models: `Guest` and `Reservation`
- JWT authentication for API clients
- Swagger/OpenAPI documentation via DRF Spectacular
- PostgreSQL-ready database configuration with SQLite fallback for development
- Docker and Gunicorn deployment support

## Enterprise role-based permissions

This backend uses `users.User.role` to enforce enterprise access:

- `admin` and Django staff users can manage hotels, branches, rooms, users, guests, and reservations.
- `manager` is reserved for future manager-level controls with read and write access.
- `receptionist` can create and modify guest and reservation records.
- `housekeeping` and `maintenance` are defined for future operational workflows.
- `guest` is the default role for authenticated users with read-only access to reservation details.

Role-based protections are enforced in DRF viewsets through `core.permissions`.

## API endpoints

- `POST /api/auth/token/` — obtain JWT access and refresh tokens
- `POST /api/auth/token/refresh/` — refresh JWT token
- `GET /api/hotels/` — list hotels
- `GET /api/branches/` — list branches
- `GET /api/room-types/` — list room types
- `GET /api/amenities/` — list amenities
- `GET /api/rooms/` — list rooms
- `GET /api/guests/` — list guests
- `GET /api/reservations/` — list reservations
- `GET /api/users/` — list enterprise users
- `GET /api/schema/` — OpenAPI schema
- `GET /api/docs/` — Swagger documentation

## Documentation

- `docs/project_architecture.md` — enterprise backend architecture
- `docs/commands.md` — command reference for development and deployment

## Deployment

Build the Docker image:

```bash
docker build -t hotel-management .
```

Run the project with Docker:

```bash
docker run -p 8000:8000 hotel-management
```

Or use Docker Compose:

```bash
docker compose up --build
```

Open:

`http://127.0.0.1:8000/`

## Next learning steps

1. Open `booking/models.py` and read how models are defined.
2. Open `booking/views.py` and see how the home view loads data.
3. Open `booking/templates/booking/home.html` to understand how templates work.
4. Use `notes/` to follow the course lessons step by step.
