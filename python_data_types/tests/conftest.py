import pytest

from introspection.models import Dog


@pytest.fixture
def dog():
    return Dog()