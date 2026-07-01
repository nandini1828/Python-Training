# Django Class 2

# Understanding settings.py

## Learning Objectives

After reading this document, you will understand:

- What `settings.py` is
- Which configuration sections are most important
- How to register a Django app
- The role of `DEBUG`, `ALLOWED_HOSTS`, and `DATABASES`
- How templates and static files are configured

## What is `settings.py`?

`settings.py` is the central configuration file of a Django project.
It controls how the entire application behaves.

Think of it as the control panel of your application.

## What Does `settings.py` Contain?

Important settings include:

- `INSTALLED_APPS`
- `DATABASES`
- `MIDDLEWARE`
- `TEMPLATES`
- `STATIC_URL`
- `MEDIA_URL`
- Security settings
- `TIME_ZONE`
- `LANGUAGE_CODE`
- `DEBUG`

## DEBUG

```python
DEBUG = True
```

- `True`: development mode
- `False`: production mode

Never deploy with `DEBUG = True`.

## INSTALLED_APPS

This list tells Django which apps should be loaded.
Whenever you create a new app, you must register it here.

Example:

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

## DATABASES

The default database is SQLite.
Later you can switch to PostgreSQL, MySQL, or other databases.

Example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## TIME_ZONE

Defines the application's timezone.

Example:

```python
TIME_ZONE = 'UTC'
```

## LANGUAGE_CODE

Defines the default language.

Example:

```python
LANGUAGE_CODE = 'en-us'
```

## STATIC_URL

Used for CSS, JavaScript, images, fonts, and other static files.

Example:

```python
STATIC_URL = 'static/'
```

## MEDIA_URL

Used for user-uploaded files like profile pictures, PDFs, and videos.

Example:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## SECRET_KEY

This key is used for security.
Never expose it publicly.
Never commit real production keys to GitHub.

## ALLOWED_HOSTS

Defines which domains can access your project.

During development, this is usually empty.
In production, it must contain your domain names.

Example:

```python
ALLOWED_HOSTS = ['example.com', 'www.example.com']
```

## Summary

`settings.py` controls almost every aspect of a Django project.
Whenever you need to configure something, the first place to check is `settings.py`.

## Interview Questions

1. What is `settings.py`?
2. What is `DEBUG`?
3. What is `INSTALLED_APPS`?
4. What is `SECRET_KEY`?
5. What is `ALLOWED_HOSTS`?
6. What is the difference between `STATIC_URL` and `MEDIA_URL`?

## Exercises

1. Open `projects/hotel_management/config/settings.py` and find the database configuration.
2. Add a comment explaining what `INSTALLED_APPS` does.
3. Try changing `TIME_ZONE` to `Asia/Kolkata` and reload the server.
