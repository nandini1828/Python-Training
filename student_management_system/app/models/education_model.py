from typing import Any, Dict, List

from pydantic import BaseModel, Field


class EducationRequest(BaseModel):
    student_name: str = Field(..., min_length=2, max_length=100)
    topics: List[str] = Field(default_factory=list)
    metadata: Dict[str, int] = Field(default_factory=dict)


class EducationResponse(BaseModel):
    student_name: str
    concepts_covered: List[str]
    summary: Dict[str, Any]
    async_demo: Dict[str, Any]
