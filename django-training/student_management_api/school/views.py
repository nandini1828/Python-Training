from rest_framework import viewsets

from .models import Student, Course, Enrollment
from .serializers import (
    StudentSerializer,
    CourseSerializer,
    EnrollmentSerializer
)


class StudentViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Student.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Course.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Enrollment.
    """

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer