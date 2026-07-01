from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AmenityViewSet, BranchViewSet, HotelViewSet, RoomTypeViewSet, RoomViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'branches', BranchViewSet)
router.register(r'room-types', RoomTypeViewSet)
router.register(r'amenities', AmenityViewSet)
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
