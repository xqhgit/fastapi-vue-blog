import json
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, root_validator, validator, Field


def json_dumps(v, *, default=None):
    for key, value in v.items():
        if isinstance(value, datetime):
            v[key] = value.strftime("%Y-%m-%d %H:%M:%S")

    return json.dumps(
        v,
        default=default,
    )


class PostCategories(BaseModel):
    __root__: List[str]

    @root_validator(pre=True)
    def root_val(cls, values):
        return {"__root__": [v.name for v in values['__root__']]}

    class Config:
        orm_mode = True


class PostComments(BaseModel):
    __root__: int

    @root_validator(pre=True)
    def root_val(cls, values):
        return {'__root__': len(values['__root__'])}

    class Config:
        orm_mode = True


class PostsListOutItem(BaseModel):
    id: int
    title: str
    description: str
    timestamp: datetime
    can_comment: bool
    is_published: bool
    categories: PostCategories
    comments: PostComments

    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S")
        }
        orm_mode = True


class PostsListOut(BaseModel):
    total: int
    items: List[PostsListOutItem]


class PostsSearchListOutItem(BaseModel):
    id: int
    title: str
    description: str
    timestamp: datetime


class PostsSearchListOut(BaseModel):
    total: int
    items: List[PostsSearchListOutItem]


class PostOutCategories(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class PostCommentsReplied(BaseModel):
    __root__: str

    @root_validator(pre=True)
    def root_val(cls, values):
        return {'__root__': values['__root__'].author}


class PostOutComments(BaseModel):
    id: int
    author: str
    body: str
    timestamp: datetime
    # 获得该评论回复谁
    replied: PostCommentsReplied = None

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    id: int
    title: str
    description: str
    body: str
    body_html: str
    timestamp: datetime
    can_comment: bool
    is_published: bool
    categories: List[PostOutCategories]
    comments: List[PostOutComments]

    class Config:
        orm_mode = True


class PostOutCreate(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class PostIn(BaseModel):
    title: str = Field(..., max_length=64)
    description: str
    body: str
    body_html: str
    can_comment: bool = False
    is_published: bool = False
    categories: List[int]


class PostInUpdate(BaseModel):
    title: str = Field(None, max_length=64)
    description: str = None
    body: str = None
    body_html: str = None
    can_comment: bool = None
    is_published: bool = None
    categories: List[int] = None


class PostOutUpdate(PostOutCreate):
    pass
