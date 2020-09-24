from pydantic import BaseModel


class PostBase(BaseModel):
    title: str


class PostCreate(PostBase):
    content: str
    is_publish: bool
    can_comment: bool
    category_id: int
    cover_image: bytes


class PostUpdate(PostBase):
    body: str
    can_comment: bool
    category_id: int

