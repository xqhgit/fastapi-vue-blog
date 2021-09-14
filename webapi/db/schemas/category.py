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

    class Config:
        orm_mode = True


class CategoryAllOutItem(BaseModel):
    id: int
    name: str
    posts: int


class CategoryAllOut(BaseModel):
    __root__: List[CategoryAllOutItem]


class CategorySelectionOutItem(BaseModel):
    id: int
    name: str


class CategorySelectionOut(BaseModel):
    __root__: List[CategorySelectionOutItem]
