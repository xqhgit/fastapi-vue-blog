from typing import Optional
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from backend.models import Category
from backend.crud.base import CRUDBase
from backend.schemas.category import CategoryCreate, CategoryUpdate


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):

    def create(self, db: Session, *, obj_in: CategoryCreate) -> Category:
        db_obj = self.model(name=obj_in.name, image=obj_in.image)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


category = CRUDCategory(Category)
