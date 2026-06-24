from __future__ import annotations

from typing import Any, Dict, Tuple


class ImmutableMatrix:
    """Immutable matrix illustrating dunder methods for container behavior."""

    def __init__(self, rows: Tuple[Tuple[int, ...], ...]) -> None:
        self._rows = rows

    def __getitem__(self, index: int) -> Tuple[int, ...]:
        return self._rows[index]

    def __len__(self) -> int:
        return len(self._rows)

    def __iter__(self):
        return iter(self._rows)

    def __repr__(self) -> str:
        rows = ", ".join(str(row) for row in self._rows)
        return f"ImmutableMatrix(({rows}))"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ImmutableMatrix):
            return False
        return self._rows == other._rows

    def transpose(self) -> "ImmutableMatrix":
        transposed = tuple(zip(*self._rows))
        return ImmutableMatrix(tuple(tuple(row) for row in transposed))


class NamingContext:
    """Demonstrates custom dunder behavior for attribute access."""

    def __init__(self, namespace: Dict[str, Any]) -> None:
        self._namespace = namespace.copy()

    def __getattr__(self, name: str) -> Any:
        if name in self._namespace:
            return self._namespace[name]
        raise AttributeError(f"Attribute {name!r} is not defined.")

    def __contains__(self, item: object) -> bool:
        return item in self._namespace

    def __repr__(self) -> str:
        return f"NamingContext({self._namespace})"
