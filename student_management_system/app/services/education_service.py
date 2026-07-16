import asyncio
from typing import Any, Dict, List

from app.models.education_model import EducationRequest, EducationResponse
from app.utils.helpers import demonstrate_python_concepts


class EducationService:
    @staticmethod
    async def build_learning_summary(request: EducationRequest) -> EducationResponse:
        concepts = [
            "Classes",
            "Type Annotations",
            "Lists",
            "Dictionaries",
            "if-else",
            "for loops",
            "break",
            "continue",
            "List Comprehension",
            "isinstance()",
            "dir()",
            "callable()",
            "Functions",
            "Modular Programming",
            "JSON Request and Response",
            "Pydantic Validation",
        ]

        filtered_topics = []
        for topic in request.topics:
            if topic:
                filtered_topics.append(topic)
                if topic.lower() == "break":
                    break
            continue

        list_comp = [topic for topic in filtered_topics if topic]
        summary = {
            "topic_count": len(list_comp),
            "concepts_count": len(concepts),
            "uses_dict": isinstance(request.metadata, dict),
            "uses_list": isinstance(request.topics, list),
            "callable_demo": callable(demonstrate_python_concepts),
        }

        await asyncio.sleep(0.05)

        return EducationResponse(
            student_name=request.student_name,
            concepts_covered=concepts,
            summary=summary,
            async_demo={
                "mode": "async",
                "awaited": True,
                "message": "FastAPI async endpoint executed successfully",
            },
        )
