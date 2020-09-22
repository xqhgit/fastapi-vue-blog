from typing import Optional, AnyStr
from pydantic import BaseModel


class AttachmentBase(BaseModel):
    pass


class AttachmentCreate(AttachmentBase):
    uid: str
    filename: str
    content_type: str
    url: str


class AttachmentUpdate(AttachmentBase):
    pass


class AttachmentDelete(AttachmentBase):
    url: str

