from typing import Optional

from pydantic import BaseModel


class ProductRequest(BaseModel):
    name: str
    price: float
    stock: int
    category: str
    description: Optional[str] = None


class CustomerRequest(BaseModel):
    name: str
    email: str
    phone: str
    address: Optional[str] = None


    #add pydantic for other models
    