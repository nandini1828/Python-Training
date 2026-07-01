from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_ADMIN = 'admin'
    ROLE_MANAGER = 'manager'
    ROLE_RECEPTIONIST = 'receptionist'
    ROLE_HOUSEKEEPING = 'housekeeping'
    ROLE_MAINTENANCE = 'maintenance'
    ROLE_GUEST = 'guest'

    ROLE_CHOICES = [
        (ROLE_ADMIN, 'Administrator'),
        (ROLE_MANAGER, 'Manager'),
        (ROLE_RECEPTIONIST, 'Receptionist'),
        (ROLE_HOUSEKEEPING, 'Housekeeping'),
        (ROLE_MAINTENANCE, 'Maintenance'),
        (ROLE_GUEST, 'Guest'),
    ]

    department = models.CharField(max_length=120, blank=True)
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default=ROLE_GUEST)
    is_employee = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    @property
    def is_receptionist(self):
        return self.role == self.ROLE_RECEPTIONIST

    @property
    def is_manager(self):
        return self.role == self.ROLE_MANAGER

    @property
    def is_housekeeping(self):
        return self.role == self.ROLE_HOUSEKEEPING

    @property
    def is_maintenance(self):
        return self.role == self.ROLE_MAINTENANCE
