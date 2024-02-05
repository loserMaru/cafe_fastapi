from typing import List, Optional
from pydantic import BaseModel
from .cafe_model import Cafe
from .drinks_model import Drinks
from .coffee_model import Coffee
from .weight_model import Weight


class OrderBase(BaseModel):
    cafe_id: int
    drinks_id: int
    coffee_id: int
    weight_id: int
    status: str
    total_price: str
    count: str
    drink_type: str


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
