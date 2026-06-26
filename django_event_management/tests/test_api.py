import pytest
from rest_framework.test import APIClient
from events.models import Organizer
client = APIClient()

@pytest.mark.django_db
def test_get_organizers():

    Organizer.objects.create(
        name="OpenAI",
        email="openai@gmail.com",
        phone="9876543210",
        company="OpenAI"
    )

    client = APIClient()

    response = client.get("/api/organizers/")

    assert response.status_code == 200

@pytest.mark.django_db
def test_create_organizer_api():

    client = APIClient()

    response = client.post(
        "/api/organizers/",
        {
            "name": "Microsoft",
            "email": "microsoft@gmail.com",
            "phone": "8888888888",
            "company": "Microsoft"
        },
        format="json"
    )

    assert response.status_code == 201