from typing import Optional
from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from backend.models import Category, Post
from backend.crud.base import CRUDBase
from backend.schemas.category import CategoryCreate, CategoryUpdate


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):

    def create(self, db: Session, *, obj_in: CategoryCreate) -> Category:
        db_obj = self.model(name=obj_in.name, image=obj_in.image)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_options(self, db: Session, *, filters=None):
        query = db.query(
            self.model.id, self.model.name
        )
        if filters is not None:
            query = query.filter(*filters)
        return [r._asdict() for r in query.all()]

    def get_list(self, db: Session):
        query = db.query(
            self.model.id, self.model.name, func.count(Post.id).label('count')
        ).outerjoin(Post).group_by(self.model.id)
        return [r._asdict() for r in query.all()]


category = CRUDCategory(Category)
