from typing import List, Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    password: str
    role: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
