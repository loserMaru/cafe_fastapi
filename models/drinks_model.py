from typing import List, Optional
from pydantic import BaseModel
from .cafe_model import Cafe


class DrinksBase(BaseModel):
    name: str
    description: str
    cafe_id: int


class DrinksCreate(DrinksBase):
    pass


class Drinks(DrinksBase):
    id: int

    class Config:
        orm_mode = True
