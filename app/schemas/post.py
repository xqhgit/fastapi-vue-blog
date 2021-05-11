from fastapi import Form
from typing import Optional, List
from pydantic import BaseModel


class PostBase(BaseModel):
    pass


class PostCreate(PostBase):
    title: str
    body: str
    category_id: int


class PostUpdate(PostBase):
    title: str
    body: str
    can_comment: bool
    category_id: int


class PostsItem(PostBase):
    id: int
    title: str
    description: str
    category: str


class PostsOut(PostBase):
    total: int
    items: List[PostsItem]


class PostCreateOut(PostBase):
    title: str


class PostListItem(PostBase):
    id: int
    title: str
    category: str


class PostListOut(PostBase):
    total: Optional[int]
    items: List[PostListItem]
