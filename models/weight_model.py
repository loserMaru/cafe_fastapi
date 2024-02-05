from typing import List, Optional
from pydantic import BaseModel
from .coffee_model import Coffee
from .drinks_model import Drinks


class WeightBase(BaseModel):
    weight: str
    price: str
    coffee_id: int
    drinks_id: int


class WeightCreate(WeightBase):
    pass


class Weight(WeightBase):
    id: int

    class Config:
        orm_mode = True
