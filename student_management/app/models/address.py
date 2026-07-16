from pydantic import BaseModel, Field


class Address(BaseModel):

    city: str = Field(..., min_length=1)
    state: str = "Unknown"

    def full_address(self) -> str:
        return f"{self.city}, {self.state}"
