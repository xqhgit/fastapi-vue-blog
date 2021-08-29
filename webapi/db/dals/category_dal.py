from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from webapi.db.models import Category
from webapi.db.schemas.category import CategoryCreate


class CategoryDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create(self, obj_in: CategoryCreate):
        db_obj = Category(**obj_in.dict())
        self.db_session.add(db_obj)
        await self.db_session.flush()
        return db_obj

    async def get_all(self) -> List[Category]:
        q = await self.db_session.execute(select(Category).order_by(Category.id))
        return q.scalars().all()
