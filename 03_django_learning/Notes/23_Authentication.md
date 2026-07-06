# Class 8: Authentication

## 1. Why Authentication matters
Authentication lets only trusted users access protected parts of an app.

## 2. Common auth concepts
- Login
- Logout
- User registration
- Permissions
- JWT tokens

## 3. JWT (JSON Web Token)
JWT is a compact token used to authenticate API requests.

### Common endpoints
- `/api/token/` for login
- `/api/token/refresh/` to refresh a token

## 4. Permissions
Permissions control what users can do.

Examples:
- Only authenticated users can access the API
- Admins can manage everything
- Regular users can view or update their own data

## 5. In this project
- The API now uses JWT authentication
- The student API requires authentication
