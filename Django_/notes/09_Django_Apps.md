# Django Class 3

# Django Apps, URL Routing & Your First View

## Learning Objectives

After this class, you will understand:

- What a Django App is
- Project vs App
- Why enterprise projects have multiple apps
- How to create an app
- App folder structure
- Registering an app
- Creating your first view
- URL routing
- Returning your first HTTP response
- How a request travels inside Django

## What is a Django App?

A Django App is a self-contained module that performs one specific functionality.

Think of it like a department in a company.

Example: In a Hotel Management System,

- `booking` app handles room reservations.
- `customers` app handles guest records.
- `rooms` app handles room availability.

This follows the software engineering principle called **Separation of Concerns**.
Each module should focus on one responsibility.

## Real Enterprise Example

Project: `Hotel Management`
Apps:

- `booking`
- `rooms`
- `customers`
- `authentication`
- `reports`

Large companies use many apps to keep code clean and manageable.

## Project vs App

| Project | App |
| --- | --- |
| Complete website or API | Small module with related feature
| Contains config and multiple apps | Contains models, views, urls, and templates
| Global settings in `config/` | Local logic inside app folder

Example:

Project: `Hotel Management`

Apps:

- `booking`
- `billing`
- `customers`
- `services`

## Step 1 — Create an App

From `projects/hotel_management/` run:

```bash
python manage.py startapp booking
```

Django creates:

```
booking/
├── admin.py
├── apps.py
├── __init__.py
├── migrations/
├── models.py
├── tests.py
├── views.py
```

Every app gets these files automatically.

## Step 2 — Register the App

Open `projects/hotel_management/config/settings.py`.
Locate `INSTALLED_APPS` and add:

```python
INSTALLED_APPS = [
    'booking',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### Why register an app?

If you do not register it, Django does not know the app exists.
It is like hiring someone but never adding them to the company system.

## Step 3 — Create Your First View

Open `booking/views.py` and add:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse('🎉 Welcome to Hotel Management System!')
```

### Understanding the code

- `from django.http import HttpResponse` imports a response class.
- `def home(request):` defines a view function.
- `request` contains HTTP request data.
- `return HttpResponse(...)` sends a response back to the browser.

## What is `request`?

Every time someone visits your website, Django creates a request object.
It contains:

- headers
- user data
- cookies
- query parameters
- body content
- HTTP method

## Step 4 — Create `booking/urls.py`

Create the file and add:

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```

### Understanding this code

- `path('', home)` means when someone visits `/`, call `home()`.

## Step 5 — Connect App URLs to Project URLs

Open `projects/hotel_management/config/urls.py` and replace it with:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),
]
```

### What is `include()`?

`include()` delegates URL handling to the app.
The project says: "Booking-related URLs? Ask the booking app." 
This keeps the project organized.

## Request Flow

When you visit `http://127.0.0.1:8000/`:

Browser
↓
`config/urls.py`
↓
`booking/urls.py`
↓
`booking/views.py`
↓
`HttpResponse`
↓
Browser

## Step 6 — Run the Server

Run:

```bash
python manage.py runserver
```

Open:

`http://127.0.0.1:8000/`

You should see:

`🎉 Welcome to Hotel Management System!`

Congratulations! You built your first Django endpoint.

## Summary

You learned:

- What a Django app is
- How to create and register an app
- How to create a view
- URL routing with `path()` and `include()`
- The request-response flow

## Interview Questions

1. What is a Django App?
2. What is the difference between a project and an app?
3. What is a view?
4. What is `HttpResponse`?
5. What is the purpose of `include()`?
6. What is `request`?

## Exercises

1. Create a new view `about()` in `booking/views.py`.
2. Add `path('about/', about, name='about')` to `booking/urls.py`.
3. Visit `/about/` in the browser.

## Mini Project Task

Add a second app called `customers` and create a simple `home` view for it.
