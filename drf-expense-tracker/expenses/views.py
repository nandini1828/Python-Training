from rest_framework.viewsets import (
    ModelViewSet
)

from .models import (
    Category,
    Expense,
    Budget
)

from .serializers import (
    CategorySerializer,
    ExpenseSerializer,
    BudgetSerializer
)


class CategoryViewSet(
    ModelViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ExpenseViewSet(
    ModelViewSet
):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class BudgetViewSet(
    ModelViewSet
):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer