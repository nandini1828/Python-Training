# Command Reference

## Purpose

This document explains the primary commands used to develop, test, and deploy the Hotel Management backend.

## Why this concept exists

A commands reference exists to ensure team members and new developers know exactly what shell commands to run and what each command does internally.

## Commands

### `pip install -r requirements.txt`

- Purpose: Installs Python dependencies.
- Syntax: `pip install -r requirements.txt`
- Internal behavior: Pip reads the requirements file, resolves package versions, downloads packages, and installs them into the active Python environment.

### `python manage.py migrate`

- Purpose: Applies database migrations.
- Syntax: `python manage.py migrate`
- Internal behavior:
  - Loads `manage.py`
  - Configures Django settings with `DJANGO_SETTINGS_MODULE`
  - Loads installed apps
  - Builds migration graph
  - Applies unapplied migrations in order
- Common errors:
  - `InconsistentMigrationHistory`
  - `django.db.utils.OperationalError`

### `python manage.py makemigrations`

- Purpose: Generates migration files from model changes.
- Syntax: `python manage.py makemigrations [app_label]`
- Internal behavior:
  - Inspects model state and database schema history
  - Creates migration operations for added/changed models or fields

### Resetting local migrations safely

For local development only, use these commands to reset the database and apply migrations from scratch:

```bash
python manage.py migrate zero
python manage.py migrate
```

If you need to regenerate migration files after schema changes:

```bash
python manage.py makemigrations
python manage.py migrate
```

> Warning: Do not use `migrate zero` on production. In production, apply migrations incrementally with `python manage.py migrate` and do not drop live data unless you have a verified backup.

### `python manage.py makemigrations`

- Purpose: Generates migration files from model changes.
- Syntax: `python manage.py makemigrations [app_label]`
- Internal behavior:
  - Inspects model state and database schema history
  - Creates migration operations for added/changed models or fields

### `python manage.py createsuperuser`

- Purpose: Creates a Django admin user.
- Syntax: `python manage.py createsuperuser`
- Internal behavior: Prompts for username/email/password and writes a new user record to the database.

### `python manage.py runserver`

- Purpose: Starts the Django development server.
- Syntax: `python manage.py runserver 127.0.0.1:8000`
- Internal behavior: Starts a lightweight local WSGI server and reloads on code changes.
- Notes: Use only for development, not production.

### `gunicorn config.wsgi:application --bind 0.0.0.0:8000`

- Purpose: Runs the project in a production-like WSGI server.
- Syntax: `gunicorn config.wsgi:application --bind 0.0.0.0:8000`
- Internal behavior: Loads the WSGI application from `config.wsgi` and listens for HTTP traffic.

### `docker compose up --build`

- Purpose: Builds Docker images and starts services.
- Syntax: `docker compose up --build`
- Internal behavior:
  - Builds container image from `Dockerfile`
  - Creates containers for each service defined in `docker-compose.yml`

## Examples

```bash
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Troubleshooting

- `ModuleNotFoundError`: Ensure the virtual environment is active and dependencies are installed.
- `InconsistentMigrationHistory`: Reset the local database or use `manage.py migrate --fake` only with care.
- `OperationalError: no such table`: Run `manage.py migrate`.

## Related commands

- `python manage.py makemigrations`
- `python manage.py test`
- `python manage.py shell`
- `python manage.py collectstatic`
