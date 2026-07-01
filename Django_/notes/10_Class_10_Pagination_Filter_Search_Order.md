# Class 10: Pagination, Filtering, Searching, Ordering

## Learning Objectives

After this class, you will understand:

- How pagination works in APIs and views
- How to filter querysets
- How to search data
- How to order results

## Pagination

Pagination divides large result sets into smaller pages.
This improves performance and user experience.

In Django ORM, you can use slicing:

```python
rooms = Room.objects.all()[0:10]
```

In DRF, use pagination classes like `PageNumberPagination`.

## Filtering

Filtering returns only the records that match conditions.

Example:

```python
available_rooms = Room.objects.filter(is_available=True)
```

Common filter examples:

- `filter(field=value)`
- `exclude(field=value)`
- `filter(price__gte=100)`
- `filter(check_in__date='2026-07-01')`

## Searching

Search lets users find records by text.
In DRF, you can use `SearchFilter`.

Example:

```python
from rest_framework.filters import SearchFilter

class RoomViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['room_number', 'room_type']
```

## Ordering

Ordering sorts results by one or more fields.

Example:

```python
rooms = Room.objects.order_by('price')
```

In DRF, use `OrderingFilter`.

## Summary

This class covered:

- pagination
- filtering
- searching
- ordering

## Interview Questions

1. What is pagination?
2. How do you filter data in Django?
3. How do you order query results?
4. What is search filtering?

## Exercises

1. Add a filter for available rooms in your home view.
2. Sort rooms by price before sending them to the template.
3. Add a search field to a DRF viewset.
