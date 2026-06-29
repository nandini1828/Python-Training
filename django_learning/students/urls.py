from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    StudentListCreateAPIView,
    about,
    home,
    student_create,
    student_delete,
    student_detail,
    student_edit,
    student_list,
)
from .viewsets import StudentViewSet

router = DefaultRouter()
router.register(r"api/v2/students", StudentViewSet, basename="student-v2")

app_name = "students"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("students/", student_list, name="student_list"),
    path("students/create/", student_create, name="student_create"),
    path("students/<int:pk>/", student_detail, name="student_detail"),
    path("students/<int:pk>/edit/", student_edit, name="student_edit"),
    path("students/<int:pk>/delete/", student_delete, name="student_delete"),
    path("api/students/", StudentListCreateAPIView.as_view(), name="student_api"),
    path("", include(router.urls)),
]