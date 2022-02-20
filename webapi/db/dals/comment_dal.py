# -*-coding:utf-8 -*-
from typing import List, Optional

from sqlalchemy import func, desc, delete
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from webapi.db.models import Comment
from webapi.db.schemas.comment import CommentCreate, CommentInUpdate


class CommentDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create(self, obj_in: CommentCreate):
        data = obj_in.dict(exclude_none=True)
        db_obj = Comment(**data)
        self.db_session.add(db_obj)
        await self.db_session.flush()
        return db_obj

    async def delete(self, *, db_obj: Comment):
        # TODO: 无法删除父评论
        await self.db_session.execute(delete(Comment).where(Comment.id == db_obj.id))

    async def update(self, db_obj: Comment, obj_in: CommentInUpdate):
        update_data = obj_in.dict(exclude_none=True)
        for field in update_data:
            setattr(db_obj, field, update_data[field])
        self.db_session.add(db_obj)
        await self.db_session.flush()
        return db_obj

    async def get_by_id(self, record_id: int, *, reviewed=None):
        stmt = select(Comment).where(Comment.id == record_id)
        if reviewed is not None:
            stmt = stmt.where(Comment.reviewed == reviewed)
        q = await self.db_session.execute(stmt)
        result = q.scalars().all()
        if result:
            return result[0]
        else:
            return None

    async def count(self, *, reviewed=None):
        stmt = select(func.count(Comment.id).label('total'))
        if reviewed is not None:
            stmt = stmt.where(Comment.reviewed == reviewed)
        q = await self.db_session.execute(stmt)
        return q.one()['total']

    async def get_limit(self, *, page, limit, reviewed=None):
        offset = limit * (page - 1)
        stmt = select(Comment).options(selectinload(Comment.post))
        if reviewed is not None:
            stmt = stmt.where(Comment.reviewed == reviewed)
        stmt = stmt.order_by(desc(Comment.timestamp)).offset(offset).limit(limit)
        q = await self.db_session.execute(stmt)
        return q.scalars().all()
