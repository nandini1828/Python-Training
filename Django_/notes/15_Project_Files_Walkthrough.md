# Project Files Walkthrough

## Learning Objectives

After reading this note, you will understand:

- the purpose of each file in `projects/hotel_management`
- how the booking app works
- where to make changes for new features

## Important project files

### `manage.py`
- runs Django commands
- starts the development server
- loads project settings

### `config/settings.py`
- global project configuration
- installed apps
- database settings
- templates and static files

### `config/urls.py`
- top-level URL routing
- includes app URL modules

### `config/wsgi.py`
- WSGI entry point for deployment

### `config/asgi.py`
- ASGI entry point for asynchronous servers

### `requirements.txt`
- lists Python package dependencies
- install with `pip install -r requirements.txt`

### `booking/models.py`
- defines the data structure:
  - `Room`
  - `Reservation`
- each model becomes a database table

### `booking/views.py`
- contains the business logic for page requests
- `home()` loads rooms and reservations for the homepage

### `booking/urls.py`
- maps `''` (the root URL) to `views.home`

### `booking/admin.py`
- registers models with the admin panel
- customizes admin list display and filters

### `booking/templates/booking/home.html`
- HTML template rendered by the `home` view
- shows available rooms and reservations

### `booking/migrations/`
- stores migration history for database changes
- contains `__init__.py` to make migrations a Python package

## How a request works in this project

1. Browser requests `http://127.0.0.1:8000/`
2. `config/urls.py` routes the request to `booking/urls.py`
3. `booking/urls.py` calls `booking.views.home`
4. `booking/views.py` loads data from models
5. Django renders `booking/templates/booking/home.html`
6. The browser receives the HTML response

## How to add a new page

1. Add a new view in `booking/views.py`
2. Add a new URL in `booking/urls.py`
3. Create a template in `booking/templates/booking/`
4. Reload the browser to see the change

## How to add a new model

1. Add a model class to `booking/models.py`
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`
4. Register the model in `booking/admin.py`

## Beginner tip

When you are unsure where a feature lives, use this pattern:

- feature appears in the browser → check `urls.py`
- logic runs in code → check `views.py`
- data is stored in the database → check `models.py`
- admin interface setup → check `admin.py`
- HTML output → check templates

## Summary

This walkthrough gives you a clear map of the sample project.
Use it as a reference while you read the class notes and inspect the code.
