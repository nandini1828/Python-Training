from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    duration = models.IntegerField()
    fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
    
class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    enrolled_on = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.course.title}"