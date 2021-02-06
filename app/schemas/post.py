from fastapi import Form
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str


class PostCreate(PostBase):
    summary: str
    content: str
    is_publish: bool
    can_comment: bool
    category_id: int
    cover_image: bytes


class PostUpdate(PostBase):
    body: str
    can_comment: bool
    category_id: int

