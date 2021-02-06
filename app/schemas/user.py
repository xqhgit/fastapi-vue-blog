from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    username: str
    password: str
    is_admin: Optional[bool]
    email: str


class UserUpdate(UserBase):
    password: Optional[str]
    email: Optional[str]






