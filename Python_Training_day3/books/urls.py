from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AuthorViewSet,
    BookViewSet,
    MemberViewSet,
)

router = DefaultRouter()

router.register(r"authors", AuthorViewSet)
router.register(r"books", BookViewSet)
router.register(r"members", MemberViewSet)

urlpatterns = [
    path("", include(router.urls)),
]