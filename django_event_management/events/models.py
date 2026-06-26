from django.db import models


class Organizer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField()
    venue = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)

    organizer = models.ForeignKey(
        Organizer,
        on_delete=models.CASCADE,
        related_name="events"
    )

    def __str__(self):
        return self.title


class Registration(models.Model):
    attendee_name = models.CharField(max_length=100)
    attendee_email = models.EmailField()
    tickets = models.IntegerField()
    payment_done = models.BooleanField(default=False)
    registered_at = models.DateTimeField(auto_now_add=True)

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="registrations"
    )

    def __str__(self):
        return self.attendee_name