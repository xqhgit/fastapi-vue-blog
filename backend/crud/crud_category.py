from typing import Optional
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from backend.models import Category
from backend.crud.base import CRUDBase
from backend.schemas.category import CategoryCreate, CategoryUpdate


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):

    pass


category = CRUDCategory(Category)
