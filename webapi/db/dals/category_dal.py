from typing import List, Optional

from sqlalchemy import update, insert, func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from webapi.db.models import Category, Post
from webapi.db.schemas.category import CategoryCreate


class CategoryDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create(self, obj_in: CategoryCreate):
        db_obj = Category(**obj_in.dict())
        self.db_session.add(db_obj)
        await self.db_session.flush()
        return db_obj

    async def get_all(self) -> List[Category]:
        sql = select(Category.id, Category.name, func.count(Post.id).label('posts')).outerjoin(Category.posts).group_by(Category.id)
        q = await self.db_session.execute(sql)
        return q.all()

    async def get_selection(self) -> List[Category]:
        q = await self.db_session.execute(select(Category).order_by(Category.id))
        return q.scalars().all()
