# -*-coding:utf-8 -*-
from typing import List, Optional
from fastapi import status
from fastapi.exceptions import HTTPException

from sqlalchemy import update, insert, func, delete
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from webapi.db.models import Category, Post
from webapi.db.schemas.category import CategoryCreate, CategoryUpdate


class CategoryDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def delete(self, *, record_id: int):
        sql = select(func.count(Post.id).label('posts')).outerjoin(Category.posts).where(Category.id == record_id)
        q = await self.db_session.execute(sql)
        posts = q.one()['posts']
        if posts:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='类别下有文章，无法删除类别')
        await self.db_session.execute(delete(Category).where(Category.id == record_id))

    async def create(self, obj_in: CategoryCreate):
        db_obj = Category(**obj_in.dict())
        self.db_session.add(db_obj)
        await self.db_session.flush()
        return db_obj

    async def update(self, db_obj: Category, obj_in: CategoryUpdate):
        db_obj.name = obj_in.name
        await self.db_session.flush()
        return db_obj

    async def count(self, name=None):
        sql = select(func.count(Category.id).label('total'))
        if name is not None:
            sql = sql.where(Category.id == name)
        q = await self.db_session.execute(sql)
        return q.one()['total']

    async def get_by_name(self, name: str):
        sql = select(Category).where(Category.name == name)
        q = await self.db_session.execute(sql)
        result = q.all()
        return result

    async def get_by_id(self, record_id: int):
        sql = select(Category).where(Category.id == record_id)
        q = await self.db_session.execute(sql)
        return q.scalars().one()

    async def get_all(self, name=None) -> List[Category]:
        sql = select(Category.id, Category.name, func.count(Post.id).label('posts')).outerjoin(Category.posts).group_by(
            Category.id)
        if name is not None:
            sql = sql.where(Category.name == name)
        q = await self.db_session.execute(sql)
        return q.all()

    async def get_limit(self, name=None, *, page, limit) -> List[Category]:
        offset = limit * (page - 1)
        sql = select(Category.id, Category.name, func.count(Post.id).label('posts')).outerjoin(Category.posts).group_by(
            Category.id)
        if name is not None:
            sql = sql.where(Category.name == name)
        sql = sql.offset(offset).limit(limit)
        q = await self.db_session.execute(sql)
        return q.all()

    async def get_selection(self) -> List[Category]:
        q = await self.db_session.execute(select(Category).order_by(Category.id))
        return q.scalars().all()
