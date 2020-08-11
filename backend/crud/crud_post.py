from typing import Optional
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from backend.models import Post
from backend.crud.base import CRUDBase
from backend.schemas.post import PostCreate, PostUpdate


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):

    def create(self, db: Session, *, obj_in: PostCreate):
        category = obj_in.category_id
        pass
        return super().create(db, obj_in=obj_in)


post = CRUDPost(Post)
