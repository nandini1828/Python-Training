# Hotel Management Project Overview

## Learning Objectives

After reading this note, you will understand:

- what the hotel management sample project includes
- how the app is structured
- how to use the REST API endpoints
- how to deploy the project with Docker

## What this project includes

The `projects/hotel_management` sample project includes:

- A Django project configuration in `config/`
- A `booking` app with rooms and reservations
- Templates for the homepage
- Static CSS for the frontend
- Django REST Framework API routes
- Docker deployment support

## Project structure

```
projects/hotel_management/
├── config/
├── booking/
├── manage.py
├── requirements.txt
├── README.md
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── static/
└── staticfiles/
```

## How the booking app works

### `booking/models.py`
Defines two models:

- `Room` — room number, type, price, and availability
- `Reservation` — guest info, room reference, check-in/check-out, and status

### `booking/views.py`
The `home` view loads available rooms and recent reservations, then renders the template.

### `booking/urls.py`
Maps the root URL (`/`) to the homepage and includes API routes under `/api/`.

### `booking/templates/booking/home.html`
The homepage template shows available rooms and recent reservations.
It also loads CSS from the `static/` folder.

## REST APIs

The project exposes API endpoints using Django REST Framework.

### Endpoints

- `GET /api/rooms/` — list all rooms
- `POST /api/rooms/` — create a new room
- `GET /api/rooms/{id}/` — retrieve a room
- `PUT /api/rooms/{id}/` — update a room
- `DELETE /api/rooms/{id}/` — delete a room

- `GET /api/reservations/` — list all reservations
- `POST /api/reservations/` — create a reservation
- `GET /api/reservations/{id}/` — retrieve a reservation
- `PUT /api/reservations/{id}/` — update a reservation
- `DELETE /api/reservations/{id}/` — delete a reservation

### Serializer behavior

- `RoomSerializer` returns room fields.
- `ReservationSerializer` returns a nested `room` object and accepts `room_id` for writes.

## Deployment with Docker

The project includes a `Dockerfile` and `docker-compose.yml`.
This makes the app deployable on any machine with Docker installed.

### Build the Docker image

```bash
docker build -t hotel-management .
```

### Run the app with Docker

```bash
docker run -p 8000:8000 hotel-management
```

### Run with Docker Compose

```bash
docker compose up --build
```

### Access the app

Open:

`http://127.0.0.1:8000/`

## Why this is a good beginner deployment example

- the project includes both web pages and API endpoints
- it uses the same Django app structure taught in the course notes
- Docker makes the deployment reproducible
- the code is small enough to read and extend

## Summary

This note explains the hotel management project end-to-end.
Use it as a companion while exploring `projects/hotel_management`.
