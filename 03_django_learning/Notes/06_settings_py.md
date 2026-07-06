# Django Class 2

# Understanding settings.py

---

# What is settings.py?

settings.py is the central configuration file of every Django project.

It controls how the entire application behaves.

Think of it as the control panel of your application.

---

# What Does settings.py Contain?

Some important settings include:

* Installed Apps
* Database Configuration
* Middleware
* Templates
* Static Files
* Media Files
* Security
* Time Zone
* Language
* Debug Mode

---

# DEBUG

```python
DEBUG = True
```

True

Development Mode

False

Production Mode

Never deploy with DEBUG=True.

---

# INSTALLED_APPS

Example:

```python
INSTALLED_APPS = [
]
```

This list tells Django which apps should be loaded.

Whenever you create a new app, you must register it here.

---

# DATABASES

Default database:

SQLite

Later we will use PostgreSQL.

Example:

```python
DATABASES = {
}
```

---

# TIME_ZONE

Defines the application's timezone.

Example:

```python
TIME_ZONE = "Asia/Kolkata"
```

---

# LANGUAGE_CODE

Defines the default language.

Example:

```python
LANGUAGE_CODE = "en-us"
```

---

# STATIC_URL

Stores CSS

JavaScript

Images

Fonts

---

# MEDIA_URL

Stores user-uploaded files.

Example:

* Profile Pictures
* PDFs
* Videos

---

# SECRET_KEY

Used for security.

Never expose this key publicly.

Never commit real production keys to GitHub.

---

# ALLOWED_HOSTS

Defines which domains can access your project.

During development:

Usually empty.

Production:

Contains your domain names.

---

# Summary

settings.py controls almost every aspect of a Django project.

Whenever you need to configure something,

the first place to check is settings.py.

---

# Interview Questions

1. What is settings.py?
2. What is DEBUG?
3. What is INSTALLED_APPS?
4. What is SECRET_KEY?
5. What is ALLOWED_HOSTS?
6. Difference between STATIC_URL and MEDIA_URL?
