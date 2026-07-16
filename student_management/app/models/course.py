from pydantic import BaseModel, Field


class Course(BaseModel):
    """
    Topics: Pydantic, class, object, list, set, tuple, dictionary, JSON,
    type casting, safe casting, type hints, and dunder methods.
    """

    name: str = Field(..., min_length=1)
    duration_weeks: int = Field(..., gt=0, le=52)
    course_id: int = 0
    enrolled_student_ids: list[int] = Field(default_factory=list)

    def summary(self) -> str:
        return f"{self.name} runs for {self.duration_weeks} weeks."

    def enroll(self, student_id: int) -> None:
        if student_id not in self.enrolled_student_ids:
            self.enrolled_student_ids.append(student_id)

    def __len__(self) -> int:
        return len(self.enrolled_student_ids)


class CourseUpdate(BaseModel):
    """Topic: Optional fields and partial update request validation."""

    name: str | None = Field(default=None, min_length=1, examples=["Python Basics"])
    duration_weeks: int | None = Field(default=None, gt=0, le=52, examples=[4])


class CourseEnrollment(BaseModel):
    """Topic: Pydantic model for validating integer IDs before enrollment."""

    course_id: int = Field(..., gt=0, examples=[1])
    student_id: int = Field(..., gt=0, examples=[1])
