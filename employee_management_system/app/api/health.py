"""Health-check endpoints for the FastAPI app."""

from fastapi import APIRouter, status

router = APIRouter()


@router.get("/health", status_code=status.HTTP_200_OK)
async def health_check() -> dict[str, str]:
    """Return a health message."""
    return {"status": "ok"}
