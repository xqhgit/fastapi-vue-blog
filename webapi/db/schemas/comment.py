from typing import Optional, List, Type
from pydantic import BaseModel, fields, EmailStr


class CommentCreateAdmin(BaseModel):
    post_id: int
    body: str
    replied_id: int = None


class CommentCreateAnonymous(CommentCreateAdmin):
    author: str = fields.Field(..., max_length=30)
    email: EmailStr = fields.Field(...)


class CommentCreate(BaseModel):
    post_id: int
    body: str
    author: str = fields.Field(..., max_length=30)
    email: EmailStr = fields.Field(...)
    from_admin: bool = False
    reviewed: bool = False
    replied_id: int = None
