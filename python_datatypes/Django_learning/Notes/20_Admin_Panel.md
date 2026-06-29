# Class 5: Admin Panel and CRUD

## 1. Django Admin Panel
- Django gives you a built-in admin panel.
- It helps manage models easily.
- To use it, create a superuser:
  - `python manage.py createsuperuser`
- Then visit:
  - `http://127.0.0.1:8000/admin/`

## 2. Registering Models
- In `students/admin.py`, register your model:
  - `admin.site.register(Student)`
- You can also use `@admin.register(Student)` for better control.

## 3. CRUD Operations
CRUD means:
- Create
- Read
- Update
- Delete

### Create
- Use forms or Django shell.
- Example:
  - `Student.objects.create(first_name="Aisha", last_name="Khan", age=20, email="aisha@example.com", course="Django")`

### Read
- Use `Student.objects.all()`
- Use `Student.objects.get(pk=1)`

### Update
- Example:
  - `student = Student.objects.get(pk=1)`
  - `student.course = "Python"`
  - `student.save()`

### Delete
- Example:
  - `student.delete()`

## 4. Basic View Pattern for CRUD
- Views handle request and response.
- Templates display data.
- Forms collect input.

## 5. Useful Commands
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`
