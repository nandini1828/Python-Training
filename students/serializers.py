from rest_framework import serializers

from .models import Course, Profile, Student


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "description", "created_at"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "bio", "location"]


class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    profile = ProfileSerializer(read_only=True, source="owner.profile")

    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "age", "email", "course", "courses", "profile", "created_at", "updated_at"]
