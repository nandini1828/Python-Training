from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .forms import StudentForm
from .models import Student
from .serializers import StudentSerializer


class StudentPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 20


class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all().order_by("-created_at")
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StudentPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["first_name", "last_name", "email", "course"]
    ordering_fields = ["created_at", "first_name", "last_name", "age"]


def home(request):
    """
    Home Page
    """
    return render(request, "students/home.html")


def about(request):
    """
    About Page
    """
    return HttpResponse("About Student Management System")


def student_list(request):
    students = Student.objects.all().order_by("-created_at")
    return render(request, "students/student_list.html", {"students": students})


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student created successfully")
            return redirect("students:student_list")
    else:
        form = StudentForm()

    return render(request, "students/student_form.html", {"form": form, "title": "Create Student"})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/student_detail.html", {"student": student})


def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully")
            return redirect("students:student_detail", pk=student.pk)
    else:
        form = StudentForm(instance=student)

    return render(request, "students/student_form.html", {"form": form, "title": "Edit Student"})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully")
        return redirect("students:student_list")

    return render(request, "students/student_confirm_delete.html", {"student": student})