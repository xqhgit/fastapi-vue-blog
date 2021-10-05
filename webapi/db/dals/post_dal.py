from typing import List, Optional
from fastapi import status
from fastapi.exceptions import HTTPException


from sqlalchemy import update, func, delete, and_
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from webapi.db.models import Post, Category, Comment, post_category
from webapi.db.schemas.post import PostIn, PostInUpdate


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

    async def update(self, db_obj: Post, obj_in: PostInUpdate):
        update_data = obj_in.dict(exclude_none=True)
        categories = await self.get_categories_by_ids(update_data.pop('categories', []))
        update_data['categories'] = categories
        for field in update_data:
            setattr(db_obj, field, update_data[field])
        self.db_session.add(db_obj)
        await self.db_session.flush()
        return db_obj

    async def delete(self, *, db_obj: Post):
        db_obj.categories = []
        await self.db_session.flush()
        await self.db_session.execute(delete(Post).where(Post.id == db_obj.id))

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

    async def exist(self, record: int):
        stmt = select(Post).where(Post.id == record)
        q = await self.db_session.execute(stmt)
        return q.scalars().one()

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
