from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Student


class StudentModelAndApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username="teacher", password="secret123")
        self.client.force_authenticate(user=self.user)
        self.student = Student.objects.create(
            first_name="Aisha",
            last_name="Khan",
            age=20,
            email="aisha@example.com",
            course="Django",
        )

    def test_student_str_representation(self):
        self.assertEqual(str(self.student), "Aisha Khan")

    def test_student_api_list_returns_students(self):
        url = reverse("students:student_api")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 1)

    def test_student_create_view_creates_student(self):
        url = reverse("students:student_create")
        response = self.client.post(
            url,
            {
                "first_name": "Bilal",
                "last_name": "Ahmed",
                "age": 22,
                "email": "bilal@example.com",
                "course": "DRF",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Student.objects.filter(email="bilal@example.com").exists())

    def test_student_api_search_filters_results(self):
        Student.objects.create(
            first_name="Bilal",
            last_name="Ahmed",
            age=25,
            email="bilal@example.com",
            course="REST",
        )

        url = reverse("students:student_api") + "?search=Aisha"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["results"][0]["first_name"], "Aisha")
