# Class 9: Relationships

## 1. ForeignKey
A ForeignKey creates a many-to-one relationship.

Example:
- One user can own many students.
- `owner = ForeignKey(User, on_delete=CASCADE)`

## 2. ManyToManyField
A ManyToManyField creates a many-to-many relationship.

Example:
- One student can belong to many courses.
- One course can have many students.

## 3. OneToOneField
A OneToOneField creates a one-to-one relationship.

Example:
- One user has one profile.

## 4. In this project
- `Student` has an owner via `ForeignKey`
- `Student` has related courses via `ManyToManyField`
- `Profile` is linked to a user via `OneToOneField`
