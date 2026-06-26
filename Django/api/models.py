from django.db import models


class Student(models.Model):
    """Represents a student in the system."""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    """Represents a course offered by the institution."""
    title = models.CharField(max_length=150)
    duration = models.CharField(max_length=50)
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    """Represents a student's course enrollment."""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.student.name} -> {self.course.title}"
