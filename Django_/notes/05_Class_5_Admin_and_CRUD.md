# Class 5: Admin Panel and CRUD

## Learning Objectives

After this class, you will understand:

- What the Django admin panel is
- How to register models with admin
- The meaning of CRUD
- How to perform Create, Read, Update, Delete operations
- How admin helps manage data during development

## What is the Django Admin Panel?

Django admin is a built-in interface for managing application data.
It is generated automatically when you register models.

Visit:

`http://127.0.0.1:8000/admin/`

## Registering Models in Admin

Open `booking/admin.py` and register models:

```python
from django.contrib import admin
from .models import Room, Reservation

admin.site.register(Room)
admin.site.register(Reservation)
```

For a better admin experience, use model admin classes:

```python
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'price', 'is_available')
```

## What is CRUD?

CRUD stands for:

- Create
- Read
- Update
- Delete

These are the main operations on application data.

## CRUD in Django

### Create

Use `Room.objects.create(...)` or admin add form.

### Read

Use `Room.objects.all()` or list view in admin.

### Update

Modify an instance and call `save()`.
Or use admin edit form.

### Delete

Call `delete()` on an instance or use admin delete action.

## Admin Best Practices

- Register only models you need to manage.
- Customize list display and filters.
- Use search fields for large datasets.
- Keep admin secure in production.

## Summary

This class covered:

- Django admin
- registering models
- CRUD operations
- admin customization

## Interview Questions

1. What is Django admin?
2. What does CRUD mean?
3. How do you register a model in admin?
4. How do you update a record using ORM?

## Exercises

1. Create a superuser with `python manage.py createsuperuser`.
2. Register the `Reservation` model in admin.
3. Use the admin site to add a room and create a reservation.
