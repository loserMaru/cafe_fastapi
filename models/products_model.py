from typing import List, Optional
from pydantic import BaseModel
from .cafe_model import Cafe
from .drinks_model import Drinks
from .coffee_model import Coffee
from .dessert_model import Dessert


class ProductsBase(BaseModel):
    cafe_id: int
    drinks_id: int
    coffee_id: int
    desert_id: int


class ProductsCreate(ProductsBase):
    pass


class Products(ProductsBase):
    id: int

    class Config:
        orm_mode = True
