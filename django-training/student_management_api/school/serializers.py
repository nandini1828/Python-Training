from rest_framework import serializers
from .models import Student, Course, Enrollment


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer for Student model.
    """

    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for Course model.
    """

    class Meta:
        model = Course
        fields = "__all__"


class EnrollmentSerializer(serializers.ModelSerializer):
    """
    Serializer for Enrollment model.
    """

    class Meta:
        model = Enrollment
        fields = "__all__"