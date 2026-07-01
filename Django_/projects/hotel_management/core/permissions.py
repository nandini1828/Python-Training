from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """Allow full access only to admin and staff users; read-only for others."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)


class IsManagerOrReadOnly(BasePermission):
    """Allow managers and admins to modify resources; read-only for others."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        if not (user and user.is_authenticated):
            return False
        return user.is_staff or getattr(user, 'role', None) == get_user_model().ROLE_MANAGER


class IsReceptionistOrAdmin(BasePermission):
    """Allow receptionists and admins to create/modify bookings and guests."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        user = request.user
        if not (user and user.is_authenticated):
            return False
        return user.is_staff or getattr(user, 'role', None) == get_user_model().ROLE_RECEPTIONIST


class IsReservationOwnerOrStaff(BasePermission):
    """Allow reservation owners and staff/receptionists to view and change reservation details."""

    def has_permission(self, request, view):
        user = request.user
        if not (user and user.is_authenticated):
            return False
        if request.method in SAFE_METHODS:
            return True
        return bool(user.is_staff or getattr(user, 'role', None) == get_user_model().ROLE_RECEPTIONIST)

    def has_object_permission(self, request, view, obj):
        user = request.user
        if not (user and user.is_authenticated):
            return False
        if request.method in SAFE_METHODS:
            if user.is_staff:
                return True
            if hasattr(obj, 'guest') and getattr(obj, 'guest', None) is not None:
                return obj.guest.email == getattr(user, 'email', None)
            return False
        return bool(user.is_staff or getattr(user, 'role', None) == get_user_model().ROLE_RECEPTIONIST)
