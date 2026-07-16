"""Report request models."""

from pydantic import BaseModel, Field


class ReportCreate(BaseModel):
    """Payload for creating a report."""

    title: str = Field(..., min_length=1)
    notes: str | None = None
