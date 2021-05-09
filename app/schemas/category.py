from typing import Optional, List
from pydantic import BaseModel


class CategoryBase(BaseModel):
    pass


class CategoryCreate(CategoryBase):
    name: str


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


class CategoryCreateOut(CategoryBase):
    name: str

    class Config:
        orm_mode = True


class CategorySelectItem(CategoryBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class CategorySelectListOut(CategoryBase):
    items: List[CategorySelectItem]
