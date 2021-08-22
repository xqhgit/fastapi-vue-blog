from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from webapi.db.models import Category


class CategoryDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_category(self, name: str):
        new_category = Category(name=name)
        self.db_session.add(new_category)
        await self.db_session.flush()

    async def get_all_categories(self) -> List[Category]:
        q = await self.db_session.execute(select(Category).order_by(Category.id))
        return q.scalars().all()
