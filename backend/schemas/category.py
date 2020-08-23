from typing import Optional, List
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    name: str
    image: bytes


class CategoryUpdate(CategoryBase):
    pass


class CategoryOut(CategoryBase):
    id: int
    name: str
    image: bytes
    timestamp: int

    class Config:
        orm_mode = True


class CategoryItems(BaseModel):
    total: Optional[int]
    items: List[CategoryOut]


