"""Simple address model used by employee records."""

from dataclasses import dataclass


@dataclass
class Address:
    """Represents an employee's address information."""

    city: str
    state: str
    country: str
    postal_code: str

    def to_dict(self) -> dict[str, str]:
        """Return the address as a dictionary."""
        return {
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "postal_code": self.postal_code,
        }
