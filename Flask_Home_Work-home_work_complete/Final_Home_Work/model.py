from pydantic import Field, BaseModel, EmailStr
from datetime import datetime


class UserIn(BaseModel):
    name: str = Field(..., max_length=32)
    surname: str = Field(..., max_length=32)
    email: EmailStr | None = Field(default=None)
    password: str = Field(..., max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(..., max_length=32)
    surname: str = Field(..., max_length=32)
    email: EmailStr | None = Field(default=None)
    password: str = Field(..., max_length=128)


class ProductIn(BaseModel):
    title: str = Field(..., max_length=50)
    description: str = Field(..., max_length=255)
    price: float = Field(...)


class Product(BaseModel):
    id: int
    title: str = Field(..., max_length=50)
    description: str = Field(..., max_length=255)
    price: float = Field(...)


class OrderIn(BaseModel):
    status_order: bool = False


class Order(BaseModel):
    id: int
    date_order: datetime
    status_order: bool
