# Django Commands Cheat Sheet

---

# Check Python Version

```bash
python --version
```

or

```bash
python3 --version
```

---

# Create Virtual Environment

```bash
python -m venv .venv
```

---

# Activate Virtual Environment

## macOS/Linux

```bash
source .venv/bin/activate
```

## Windows CMD

```cmd
.venv\Scripts\activate
```

## Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

# Verify Python Path

macOS/Linux

```bash
which python
```

Windows

```cmd
where python
```

---

# Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

# Install Django

```bash
pip install django
```

---

# Verify Django Version

```bash
django-admin --version
```

---

# Save Installed Packages

```bash
pip freeze > requirements.txt
```

---

# Install Packages from requirements.txt

```bash
pip install -r requirements.txt
```

---

# Create Django Project

```bash
django-admin startproject config .
```

---

# Run Development Server

```bash
python manage.py runserver
```

---

# Run on Custom Port

```bash
python manage.py runserver 9000
```

---

# Stop Server

Press

CTRL + C

---

# Deactivate Virtual Environment

```bash
deactivate
```
