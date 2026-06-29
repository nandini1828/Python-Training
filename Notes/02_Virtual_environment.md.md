# Django - Class 1

# Virtual Environment

---

# What is a Virtual Environment?

A Virtual Environment (venv) is an isolated Python environment created for a specific project.

Each project gets its own:

- Python Packages
- Dependencies
- Installed Libraries

This prevents conflicts between projects.

---

# Why Do We Need It?

Imagine:

Project A

Uses

Django 5.2

Project B

Uses

Django 4.2

Without Virtual Environment:

Only one version can exist globally.

Projects will break.

With Virtual Environment:

Project A

↓

Own Django Version

Project B

↓

Own Django Version

No conflicts.

---

# What happens when we create a venv?

Python creates a folder called:

.venv

Inside it:

- Python Interpreter
- pip
- Installed Packages
- Scripts

Everything remains isolated.

---

# Why ".venv"?

The dot (.) makes the folder hidden on Linux/macOS.

It keeps the project cleaner.

---

# Activation

Before installing packages:

Always Activate.

Mac/Linux

source .venv/bin/activate

Windows

.venv\Scripts\activate

---

# How do we know it's activated?

Your terminal changes from

$

to

(.venv)

Example

(.venv)

student_management %

---

# Deactivation

Simply type

deactivate

---

# Best Practices

✔ Create one virtual environment per project.

✔ Never commit .venv to Git.

✔ Always commit requirements.txt.

✔ Activate before working.

---

# Common Mistakes

Installing packages globally.

Not activating venv.

Deleting requirements.txt.

Using multiple Django versions globally.

---

# Interview Questions

What is Virtual Environment?

Why do we use Virtual Environment?

What is pip?

What is requirements.txt?
