from .inspector import (
    get_type,
    get_id,
    get_all_attributes,
    get_public_attributes,
    get_doc,
    get_methods,
    get_methods_with_docs,
)

from .models import Animal, Dog, Student

__all__ = [
    "Animal",
    "Dog",
    "Student",
    "get_type",
    "get_id",
    "get_all_attributes",
    "get_public_attributes",
    "get_doc",
    "get_methods",
    "get_methods_with_docs",
]