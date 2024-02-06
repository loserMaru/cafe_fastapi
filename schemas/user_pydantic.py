from typing import Optional

from pydantic import BaseModel, EmailStr, constr, validator, Field


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    email: EmailStr
    password: constr(min_length=8)

    @validator("email")
    def email_must_contain_at(cls, v):
        if "@" not in v:
            raise ValueError("invalid email")
        return v


class UserUpdate(UserBase):
    password: str
    role: str


class User(UserBase):
    id: int
    role: Optional[str] = Field(default="user")

    class Config:
        from_attributes = True
