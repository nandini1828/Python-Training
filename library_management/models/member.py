from pydantic import BaseModel, Field


class MemberBase(BaseModel):
    name: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)


class MemberCreate(MemberBase):
    pass


class MemberRead(MemberBase):
    id: int
