# Workspace Tour

## Learning Objectives

After reading this note, you will understand:

- the purpose of each top-level folder
- the key files inside the sample Django project
- how the notes are organized
- what to read first as a beginner

## Workspace Structure

```
Django_/
├── commands/
├── notes/
├── projects/
│   └── hotel_management/
│       ├── config/
│       ├── booking/
│       ├── manage.py
│       ├── requirements.txt
│       └── README.md
├── resources/
└── README.md
```

## Top-level folders

### `commands/`
This folder contains command references for Django.
For example, `commands/manage_py_commands.md` shows common `manage.py` commands.

### `notes/`
This is the main learning folder.
It contains class notes organized by lesson.
Begin with `notes/00_Workspace_Guide.md` and `notes/00_Django_Course_Roadmap.md`.

### `projects/`
This folder contains practical Django examples.
The `hotel_management` project is the app you can run and explore.

### `resources/`
A placeholder for diagrams, images, and additional study material.

### `README.md`
The workspace introduction and quick start guide.

## Inside `projects/hotel_management/`

```
hotel_management/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── booking/
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── README.md
└── requirements.txt
```

## Key project files explained

### `manage.py`
This file runs Django commands for the project.
It loads the settings and starts the server.

### `config/settings.py`
This is the main configuration file.
It defines installed apps, database settings, templates, middleware, and static files.

### `config/urls.py`
This file maps root URLs to the app URL files.
It connects the project to the `booking` app routes.

### `booking/models.py`
This file defines the data structure for rooms and reservations.
Each model maps to a database table.

### `booking/views.py`
This file contains the code that runs when a user visits a web page.
The `home` view loads room and reservation data.

### `booking/urls.py`
This file defines app-specific routes.
It maps `/` to the `home` view.

### `booking/templates/booking/home.html`
This file is the HTML template used by the `home` view.
It displays available rooms and recent reservations.

### `booking/admin.py`
This file registers models with the Django admin panel.
It customizes how rooms and reservations appear in admin.

### `requirements.txt`
This file lists the Python packages needed for the project.
Install them with `pip install -r requirements.txt`.

### `projects/hotel_management/README.md`
This file provides setup instructions for the sample project.

## Recommended learning order

1. `notes/00_Workspace_Guide.md`
2. `notes/00_Django_Course_Roadmap.md`
3. `notes/01_Class_1_Intro_To_Django.md`
4. `notes/02_Class_2_Project_Structure_and_Templates.md`
5. `notes/03_Class_3_Apps_Settings_and_Urls.md`
6. Open and inspect the sample project files
7. Continue with the remaining class notes in order

## How to use the sample project

1. Open `projects/hotel_management/README.md`.
2. Activate the virtual environment.
3. Install packages.
4. Run migrations.
5. Start the server.
6. Visit `http://127.0.0.1:8000/` in your browser.

## Notes for beginners

- Read each notes file slowly.
- After each class note, open the related project files.
- Run the project and try changing small things.
- Use `commands/manage_py_commands.md` when you need exact commands.

## Summary

This note helps you understand the workspace layout and where to find each learning resource.
Follow it before you start coding so the full learning path makes sense.
