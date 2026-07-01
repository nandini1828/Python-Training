from rest_framework.routers import DefaultRouter
from hotels.views import AmenityViewSet, BranchViewSet, HotelViewSet, RoomTypeViewSet, RoomViewSet
from bookings.views import GuestViewSet, ReservationViewSet
from users.views import UserViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'branches', BranchViewSet)
router.register(r'room-types', RoomTypeViewSet)
router.register(r'amenities', AmenityViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'guests', GuestViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'users', UserViewSet)
