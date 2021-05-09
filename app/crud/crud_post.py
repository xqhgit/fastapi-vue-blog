from typing import Optional, Tuple
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app import crud
from app.models import Post
from app.crud.base import CRUDBase
from app.schemas.post import PostCreate, PostUpdate


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):

    def create(self, db: Session, *, obj_in: PostCreate) -> Post:
        category = crud.category.get(db, id=obj_in.category_id)
        if not category:
            raise ValueError
        return super().create(db, obj_in=obj_in)


post = CRUDPost(Post)
