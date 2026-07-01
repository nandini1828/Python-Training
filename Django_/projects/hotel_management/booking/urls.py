from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .api import GuestViewSet, RoomViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'guests', GuestViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('reservation-confirmation/<int:reservation_id>/', views.reservation_confirmation, name='reservation_confirmation'),
    path('manage/', views.manage_reservations, name='manage_reservations'),
    path('manage/<int:reservation_id>/<str:action>/', views.manage_reservation_action, name='manage_reservation_action'),
]
