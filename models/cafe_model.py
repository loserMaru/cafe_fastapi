from typing import List, Optional
from pydantic import BaseModel


class CafeBase(BaseModel):
    name: str
    address: str
    description: str


class CafeCreate(CafeBase):
    pass


class Cafe(CafeBase):
    id: int

    class Config:
        orm_mode = True
