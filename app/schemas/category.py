from typing import Optional, List
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryOut(CategoryBase):
    id: int
    name: str
    count: int

    class Config:
        orm_mode = True


class CategoryItems(BaseModel):
    total: Optional[int]
    items: List[CategoryOut]


