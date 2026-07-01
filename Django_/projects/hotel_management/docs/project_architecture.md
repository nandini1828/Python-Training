# Project Architecture

## Purpose

This document describes the architecture of the Hotel Management backend project, with a focus on how Django, Django REST Framework, JWT authentication, and enterprise app modules are organized.

## Why this concept exists

A clear architecture document exists to help developers understand how requests move through the system, which components are responsible for each feature, and how modules are separated for enterprise-scale maintenance.

## Problems it solves

- Prevents confusion about where business logic lives
- Enables consistent API design across modules
- Supports scalable addition of new hotel, booking, user, and admin features
- Reduces coupling between frontend, API, and data models

## Internal workflow

### HTTP request lifecycle

Browser / API Client
↓
DNS / TCP / HTTP
↓
Django development server / Gunicorn
↓
WSGI
↓
`config.settings`
↓
Middleware stack
↓
URL resolver
↓
View or ViewSet
↓
Serializers / ORM
↓
Database query
↓
ORM model instances
↓
Response object
↓
Middleware
↓
WSGI
↓
HTTP response
↓
Browser / API client

## Enterprise usage

This architecture isolates business domains into separate Django apps:

- `users` for authentication and enterprise user profiles
- `hotels` for hotel inventory, branches, room types, amenities, and rooms
- `bookings` for API exposure of reservations and guest data
- `booking` for legacy guest booking frontend and reservation workflow
- `core` for shared permissions and cross-cutting concerns

This keeps modules loosely coupled and makes the backend maintainable in large teams.

## How this project uses it

### URL configuration

- `config/urls.py` exposes the admin panel, login/logout pages, API schema, Swagger UI, JWT endpoints, and the single API router.
- `config/routers.py` centralizes API route registration for enterprise apps.
- `hotels/urls.py`, `bookings/urls.py`, and `users/urls.py` define the app-level routers.

### App responsibilities

- `hotels` manages hotel catalog data and room inventory.
- `bookings` provides REST endpoints for guest and reservation management.
- `users` exposes enterprise user CRUD operations.
- `booking` continues to serve the user-facing legacy booking pages and admin management.

## Workflow diagrams

API request flow:

```
Client -> Django URL config -> config.routers -> ViewSet -> Serializer -> ORM -> Database
```

JWT login flow:

```
Client POST /api/auth/token/ -> SimpleJWT -> validate credentials -> return access/refresh tokens
```

## Code explanation

### `config/urls.py`

This file is the entry point for incoming HTTP requests. It defines:

- `admin/` for Django admin
- `accounts/login/` and `accounts/logout/` for session auth
- `api/schema/` and `api/docs/` for OpenAPI documentation
- `api/auth/` for JWT token endpoints
- `api/` for all API viewsets registered in `config/routers.py`
- `` for the legacy booking frontend

### `config/routers.py`

This file centralizes router registration so enterprise APIs share a single consistent route prefix. It imports viewsets from each app and registers them with `DefaultRouter`.

## Common mistakes

- Adding app routes directly in multiple URL configuration files instead of using central routing.
- Mixing frontend-only apps with API-only apps without clear module separation.
- Using the default Django user model after the custom user model is active.

## Best practices

- Keep each domain model in its own app.
- Use shared router configuration for API consistency.
- Write documentation for each app and each command.
- Keep `AUTH_USER_MODEL` stable once migrations are applied.

## Debugging tips

- If `manage.py migrate` fails with `InconsistentMigrationHistory`, inspect migration dependencies and reset the development database.
- If a module import fails, verify `INSTALLED_APPS` and package names.
- If a route is not found, print `settings.ROOT_URLCONF` and inspect `config/urls.py`.

## Performance considerations

- Use `select_related` and `prefetch_related` in viewsets to prevent N+1 queries.
- Limit the results returned by list endpoints using pagination.
- Keep static and media serving separate from the Django process in production.

## Security considerations

- Use JWT tokens for API authentication.
- Keep `DEBUG=False` in production.
- Use `ALLOWED_HOSTS` and environment variables for configuration.
- Separate session-based admin login from API token authentication.
- Use role-based permission classes to limit who can create, update, and delete enterprise resources.

## Enterprise role-based permissions

The application stores enterprise roles in `users.User.role` and uses them to enforce access in API endpoints.

- `admin` and Django staff users retain full management rights through DRF viewsets.
- `receptionist` can manage guest and reservation workflows.
- `manager` is reserved for broader management functions.
- `housekeeping` and `maintenance` roles are available for future operational extensions.
- `guest` represents default authenticated users with read-only reservation access.

This separation supports a production-ready permission model for enterprise hotel operations.

## Interview questions

- Why separate `users`, `hotels`, and `bookings` into different Django apps?
- How does Django resolve a request to a view or viewset?
- What is the role of `AUTH_USER_MODEL` in a Django project?
- Why use `DefaultRouter` with DRF viewsets?

## Summary

This project architecture document maps enterprise modules to Django app boundaries and explains how the backend handles requests from incoming HTTP traffic to persisted database objects.

## References

- `config/settings.py`
- `config/urls.py`
- `config/routers.py`
- `hotels/models.py`
- `bookings/views.py`
- `users/models.py`
