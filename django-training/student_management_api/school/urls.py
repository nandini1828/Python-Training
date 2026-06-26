from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet,
    CourseViewSet,
    EnrollmentViewSet,
)

# Create a router
router = DefaultRouter()

# Register ViewSets
router.register(r"students", StudentViewSet)
router.register(r"courses", CourseViewSet)
router.register(r"enrollments", EnrollmentViewSet)

# Expose router URLs
urlpatterns = router.urls