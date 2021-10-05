# -*-coding:utf-8 -*-
from typing import List, Optional

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from webapi.db.models import Comment
from webapi.db.schemas.comment import CommentCreate


class CommentDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create(self, obj_in: CommentCreate):
        data = obj_in.dict(exclude_none=True)
        db_obj = Comment(**data)
        self.db_session.add(db_obj)
        await self.db_session.flush()
        return db_obj
