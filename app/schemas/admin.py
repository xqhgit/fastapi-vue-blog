from typing import Optional
from pydantic import BaseModel


class AdminBase(BaseModel):
    pass


class AdminCreate(AdminBase):
    username: str
    password: str
    email: str


class AdminUpdate(AdminBase):
    password: Optional[str]
    email: Optional[str]






