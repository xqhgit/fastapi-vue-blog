from typing import List, Optional

from sqlalchemy import update, func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from webapi.db.models import Post, Category
from webapi.db.schemas.post import PostIn


class PostDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        # self.db_session.run_sync()

    async def get_categories_by_ids(self, ids: List[int]):
        stmt = select(Category).where(Category.id.in_(ids))
        q = await self.db_session.execute(stmt)
        return q.scalars().all()

    def sync_create(self, session, db_obj):
        session.add(db_obj)
        session.flush()
        return db_obj

    async def create(self, obj_in: PostIn):
        data = obj_in.dict()
        categories = await self.get_categories_by_ids(data.pop('categories', []))
        db_obj = Post(**data)
        db_obj.categories.extend(categories)
        self.db_session.add(db_obj)
        await self.db_session.flush()
        return db_obj

    async def count(self, title=None):
        stmt = select(func.count(Post.id).label('total'))
        if title is not None:
            stmt = stmt.where(Post.title.like(f'%{title}%'))
        q = await self.db_session.execute(stmt)
        return q.one()['total']

    async def get_by_title(self, title: str):
        sql = select(Post).where(Post.title == title)
        q = await self.db_session.execute(sql)
        return q.all()

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
