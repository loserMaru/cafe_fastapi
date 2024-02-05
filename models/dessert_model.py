from typing import List, Optional
from pydantic import BaseModel


class DessertBase(BaseModel):
    pass


class DessertCreate(DessertBase):
    pass


class Dessert(DessertBase):
    id: int

    class Config:
        orm_mode = True
