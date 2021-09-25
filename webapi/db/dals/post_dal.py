from typing import List, Optional

from sqlalchemy import update, func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from webapi.db.models import Post


class PostDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def count(self, title=None):
        stmt = select(func.count(Post.id).label('total'))
        if title is not None:
            stmt = stmt.where(Post.title.like(f'%{title}%'))
        q = await self.db_session.execute(stmt)
        return q.one()['total']

    # async def get_all_posts(self) -> List[Post]:
    #     q = await self.db_session.execute(select(Post).order_by(Post.id))
    #     return q.scalars().all()

    async def get_by_id(self, record_id: int):
        stmt = select(Post).options(selectinload(Post.categories), selectinload(Post.comments)).where(
            Post.id == record_id)
        q = await self.db_session.execute(stmt)
        return q.scalars().one()

    async def get_limit(self, title=None, *, page, limit) -> List[Post]:
        offset = limit * (page - 1)
        stmt = select(Post).options(selectinload(Post.categories), selectinload(Post.comments))
        if title is not None:
            stmt = stmt.where(Post.title.like(f'%{title}%'))
        stmt = stmt.offset(offset).limit(limit)
        q = await self.db_session.execute(stmt)
        return q.scalars().all()
