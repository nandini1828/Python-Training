# Class 9: Relationships — ForeignKey, ManyToMany, OneToOne

## Learning Objectives

After this class, you will understand:

- What `ForeignKey` is
- What `ManyToManyField` is
- What `OneToOneField` is
- How to model relationships in Django
- When to use each relationship type

## Relationship Types in Django

### ForeignKey

A `ForeignKey` creates a many-to-one relationship.
Example: A reservation belongs to one room.

```python
class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
```

This means multiple reservations can reference the same room.

### ManyToManyField

A `ManyToManyField` creates a many-to-many relationship.
Example: A guest can have multiple services and a service can belong to many guests.

```python
class Service(models.Model):
    name = models.CharField(max_length=50)

class Guest(models.Model):
    services = models.ManyToManyField(Service)
```

### OneToOneField

A `OneToOneField` creates a one-to-one relationship.
Example: A user has one profile.

```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
```

## When to Use Each Relationship

- `ForeignKey`: use when many items relate to one item.
- `ManyToManyField`: use when items relate to many items both ways.
- `OneToOneField`: use when one item pairs with exactly one other item.

## Why Relationships Matter

Relationships model real-world data accurately.
They let you query related objects efficiently.

## Summary

This class covered:

- ForeignKey
- ManyToManyField
- OneToOneField
- relationship design

## Interview Questions

1. What is a ForeignKey?
2. What is a ManyToManyField?
3. When should you use OneToOneField?
4. How does Django represent relationships in the database?

## Exercises

1. Add a `Guest` model with a foreign key to `Reservation`.
2. Add a `Service` model and connect it with `Guest` using `ManyToManyField`.
3. Create a simple `UserProfile` model using `OneToOneField`.
