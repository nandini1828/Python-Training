from rest_framework.routers import DefaultRouter

from .views import (
    OrganizerViewSet,
    EventViewSet,
    RegistrationViewSet,
)

router = DefaultRouter()
router.register(r'organizers', OrganizerViewSet)
router.register(r'events', EventViewSet)
router.register(r'registrations', RegistrationViewSet)

urlpatterns = router.urls