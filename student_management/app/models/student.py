from pydantic import BaseModel, Field
from app.models.address import Address


class Student(BaseModel):
    """
    Topics: Pydantic, class, object, self, methods, list, type hints,
    composition, truthiness, introspection, and dunder methods.
    """

    name: str = Field(..., min_length=1)
    age: int = Field(..., gt=0, lt=120)
    address: Address
    student_id: int = 0
    courses: list[str] = Field(default_factory=list)

    def introduce(self) -> str:
        return f"Hi, I am {self.name}, I am {self.age} years old."

    def add_course(self, course_name: str) -> None:
        if course_name not in self.courses:
            self.courses.append(course_name)

    def __str__(self) -> str:
        return f"{self.name} from {self.address.city}"

    def __len__(self) -> int:
        return len(self.courses)


class StudentInput(BaseModel):
    """Topic: Pydantic request body validation for creating a student."""

    name: str = Field(..., min_length=1, examples=["Asha"])
    age: int = Field(..., gt=0, lt=120, examples=[20])
    city: str = Field(..., min_length=1, examples=["Pune"])


class StudentUpdate(BaseModel):
    """Topic: Optional fields, None, safe updates, and Pydantic validation."""

    name: str | None = Field(default=None, min_length=1, examples=["Rahul"])
    age: int | None = Field(default=None, gt=0, lt=120, examples=[21])
    city: str | None = Field(default=None, min_length=1, examples=["Mumbai"])
