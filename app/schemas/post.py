from fastapi import Form
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
