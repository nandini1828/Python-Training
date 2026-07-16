from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    isbn: str = Field(..., min_length=1)
    status: int = 0


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    id: int
