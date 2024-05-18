from pydantic import Field, BaseModel, EmailStr


class UserIn(BaseModel):
    name: str = Field(..., max_length=32, )
    email: EmailStr | None = Field(default=None)
    password: str = Field(..., max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(..., max_length=32)
    email: EmailStr | None = Field(default=None)
    password: str = Field(..., max_length=128)
