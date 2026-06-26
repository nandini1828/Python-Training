from django.db import models


class Student(models.Model):
    """
    Stores student information.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    """
    Stores course information.
    """

    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, unique=True)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name


class Enrollment(models.Model):
    """
    Connects a Student with a Course.
    """

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    enrolled_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.course.course_name}"