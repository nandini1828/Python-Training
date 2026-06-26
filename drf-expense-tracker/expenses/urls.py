from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    CategoryViewSet,
    ExpenseViewSet,
    BudgetViewSet
)

router = DefaultRouter()

router.register(
    "categories",
    CategoryViewSet
)

router.register(
    "expenses",
    ExpenseViewSet
)

router.register(
    "budgets",
    BudgetViewSet
)

urlpatterns = router.urls