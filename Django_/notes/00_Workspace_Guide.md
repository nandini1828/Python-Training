# Django Workspace Guide

This workspace is designed to teach Django from beginner to advanced.
It contains lesson notes, command references, and a working Django project.

## What this workspace contains

- `README.md` — the main introduction and quick start guide
- `notes/` — class notes and learning documents
- `commands/` — Django command reference for beginners
- `projects/hotel_management/` — a sample Django application with code
- `resources/` — place for future assets, diagrams, and reference files

## How to learn from this workspace

1. Start with `notes/00_Django_Course_Roadmap.md`.
2. Follow the class notes in order: `01_Class_1_...`, `02_Class_2_...`, etc.
3. Use `commands/django_commands.md` for the most common command examples.
4. Open the sample project in `projects/hotel_management/` and inspect the files.
5. Run the project using the instructions in `projects/hotel_management/README.md`.

## Folder structure explained

### `notes/`
Contains lesson documents for each class.
The class note files are the best place to start.

### `commands/`
Contains useful Django CLI commands and examples.
This is where you can find the commands to run the server, create apps, and manage migrations.

### `projects/hotel_management/`
This is a fully scaffolded Django project.
It includes a `booking` app, configuration files, and a simple hotel booking interface.

### `projects/hotel_management/config/`
Contains the Django configuration package:

- `settings.py` — project configuration
- `urls.py` — URL routing for the project
- `wsgi.py` — WSGI application entrypoint
- `asgi.py` — ASGI application entrypoint

### `projects/hotel_management/booking/`
Contains the hotel booking app:

- `models.py` — data models for rooms and reservations
- `views.py` — request handlers for the homepage
- `urls.py` — app-level URL routing
- `admin.py` — admin registration
- `templates/` — HTML templates

## How to read the code

Begin with these files:

- `projects/hotel_management/manage.py`
- `projects/hotel_management/config/settings.py`
- `projects/hotel_management/config/urls.py`
- `projects/hotel_management/booking/views.py`
- `projects/hotel_management/booking/models.py`
- `projects/hotel_management/booking/templates/booking/home.html`

These files show how Django connects a request from the browser to a view and returns an HTML page.

## Why this workspace is beginner-friendly

- Notes use plain language and step-by-step explanations.
- The course roadmap shows what to learn in each class.
- The sample project is small and easy to explore.
- The command file shows the exact commands to run.

## Recommended learning path

1. `README.md`
2. `notes/00_Django_Course_Roadmap.md`
3. `notes/01_Class_1_Intro_To_Django.md`
4. `notes/02_Class_2_Project_Structure_and_Templates.md`
5. `notes/03_Class_3_Apps_Settings_and_Urls.md`
6. Continue through `notes/11_Class_11_Deployment_Docker_Gunicorn_Nginx.md`

## Important note

If you are new to Django, start with `notes/01_Class_1_Intro_To_Django.md` and follow the notes in numerical order.
Read the project files after each class to see the concepts in real code.
