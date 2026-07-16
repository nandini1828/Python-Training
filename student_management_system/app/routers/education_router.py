from fastapi import APIRouter, status

from app.models.education_model import EducationRequest, EducationResponse
from app.services.education_service import EducationService

router = APIRouter(prefix="/education", tags=["Education"])


@router.post("", response_model=EducationResponse, status_code=status.HTTP_200_OK)
async def education_demo(request: EducationRequest):
    return await EducationService.build_learning_summary(request)
