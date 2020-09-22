import uuid
import shutil
import os
from urllib.parse import urljoin
from fastapi import UploadFile, requests
from starlette.requests import Request
from typing import Union, Dict
from sqlalchemy.orm import Session

from backend.core.config import settings
from backend.models import Attachment
from backend.crud.base import CRUDBase
from backend.schemas.attachment import AttachmentCreate, AttachmentUpdate


class CRUDAttachment(CRUDBase[Attachment, AttachmentCreate, AttachmentUpdate]):

    def create_by_file(self, db: Session, *, file: UploadFile, request: Request):
        uid = str(uuid.uuid4())
        file_url = self.save_file(file=file, uid=uid, request=request)
        obj_in = AttachmentCreate(
            filename=file.filename, content_type=file.content_type,
            uid=uid, url=file_url
        )
        db_obj = self.create(db, obj_in=obj_in)
        return db_obj

    def delete_by_url(self, db: Session, *, url: str):
        db.query(self.model).filter(self.model.url == url).delete()
        db.commit()

    def save_file(self, *, file: UploadFile, uid, request: Request) -> str:
        file_object = file.file
        file_path = os.path.join(settings.BASEDIR, 'static/attachments/{}'.format(uid))
        file_url = urljoin(str(request.base_url), '/static/attachments/{}'.format(uid))
        # save attachment
        with open(file_path, 'wb+') as folder:
            shutil.copyfileobj(file_object, folder)
        return file_url


attachment = CRUDAttachment(Attachment)
