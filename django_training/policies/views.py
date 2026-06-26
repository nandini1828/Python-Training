from rest_framework import viewsets

from .models import Policy
from .serializers import PolicySerializer


class PolicyViewSet(viewsets.ModelViewSet):
    """
    CRUD API for Policy model.
    """

    queryset = Policy.objects.all()
    serializer_class = PolicySerializer