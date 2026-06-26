import pytest
from events.models import Organizer
from events.models import Event
from datetime import date

@pytest.mark.django_db
def test_create_organizer():

    organizer = Organizer.objects.create(
        name="OpenAI",
        email="openai@gmail.com",
        phone="9876543210",
        company="OpenAI"
    )

    assert organizer.name == "OpenAI"
    assert organizer.email == "openai@gmail.com"

@pytest.mark.django_db
def test_create_event():

    organizer = Organizer.objects.create(
        name="Google",
        email="google@gmail.com",
        phone="9999999999",
        company="Google"
    )

    event = Event.objects.create(
        title="Python Workshop",
        description="Learn Django",
        date=date.today(),
        venue="Hyderabad",
        price=499.99,
        organizer=organizer
    )

    assert event.title == "Python Workshop"
    assert event.organizer.name == "Google"