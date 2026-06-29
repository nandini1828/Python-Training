# Django Installation

---

# Installing Django

After creating and activating the virtual environment:

Install Django using pip.

pip install django

---

# Verify Installation

django-admin --version

---

# Why upgrade pip?

Older versions may contain bugs.

Always upgrade.

python -m pip install --upgrade pip

---

# requirements.txt

Store installed packages.

pip freeze > requirements.txt

Anyone can recreate the environment.

pip install -r requirements.txt

---

# Django Project

Create Project

django-admin startproject config .

Notice the dot (.)

Without dot

project/project/

With dot

project/

manage.py

config/

Cleaner structure.

---

# Running Server

python manage.py runserver

Open

http://127.0.0.1:8000/

You should see

"The install worked successfully!"

---

# Development Server

The built-in server is only for development.

Production uses

Gunicorn

uWSGI

Daphne

etc.

---

# What We Learned

✔ Install Django

✔ Verify Installation

✔ Create Project

✔ Run Server

✔ requirements.txt
