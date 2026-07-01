# Class 8: Authentication, JWT, and Permissions

## Learning Objectives

After this class, you will understand:

- What authentication is in APIs
- What JWT is
- How permissions protect resources
- How to secure API endpoints

## What is Authentication?

Authentication verifies the identity of a user.
In APIs, this means checking a token or credentials.

Common methods:

- session authentication
- token authentication
- JWT authentication

## What is JWT?

JWT stands for JSON Web Token.
It is a secure token used to authenticate users across requests.

A JWT has three parts:

- header
- payload
- signature

Example flow:

1. User logs in.
2. Server returns a JWT.
3. Client sends JWT with each API request.
4. Server validates the token.

## What are Permissions?

Permissions determine what a user can do.
DRF permissions help protect API access.

Examples:

- `IsAuthenticated`
- `IsAdminUser`
- `AllowAny`

## Protecting API Endpoints

Use DRF settings and view permission classes.

Example:

```python
from rest_framework.permissions import IsAuthenticated

class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
```

## Summary

This class covered:

- API authentication
- JWT tokens
- permissions
- securing endpoints

## Interview Questions

1. What is JWT?
2. Why do we use permissions?
3. What is authentication?
4. What does `IsAuthenticated` do?

## Exercises

1. Add `djangorestframework-simplejwt` to requirements.
2. Configure JWT authentication in DRF.
3. Secure the room API with `IsAuthenticated`.
