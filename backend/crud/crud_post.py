from typing import Optional
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from backend import crud
from backend.models import Post
from backend.crud.base import CRUDBase
from backend.schemas.post import PostCreate, PostUpdate


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):

    def create(self, db: Session, *, obj_in: PostCreate):
        category = crud.category.get(db, id=obj_in.category_id)
        if not category:
            raise ValueError
        db_obj = self.model(
         **obj_in.dict()
        )
        return db_obj


post = CRUDPost(Post)
