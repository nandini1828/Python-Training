from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet, ProjectViewSet

router = DefaultRouter()

router.register(r"departments", DepartmentViewSet)
router.register(r"employees", EmployeeViewSet)
router.register(r"projects", ProjectViewSet)

urlpatterns = router.urls