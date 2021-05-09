from typing import Optional, AnyStr
from pydantic import BaseModel, EmailStr


class CommentBase(BaseModel):
    pass


class CommentCreate(CommentBase):
    post_id: int
    body: str
    author: str
    email: EmailStr


class CommentUpdate(CommentBase):
    pass


class CommentDelete(CommentBase):
    pass

