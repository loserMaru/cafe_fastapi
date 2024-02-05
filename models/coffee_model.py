from typing import List, Optional
from pydantic import BaseModel


class CoffeeBase(BaseModel):
    name: str
    description: str
    location: str


class CoffeeCreate(CoffeeBase):
    pass


class Coffee(CoffeeBase):
    id: int

    class Config:
        orm_mode = True
