from fastapi import Form
from typing import Optional, List
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str


class PostCreate(PostBase):
    body: str
    category_id: int


class PostUpdate(PostBase):
    body: str
    can_comment: bool
    category_id: int


class PostCreateOut(PostBase):
    title: str


class PostListItem(PostBase):
    id: int
    title: str
    category: str


class PostListOut(PostBase):
    total: Optional[int]
    items: List[PostListItem]
