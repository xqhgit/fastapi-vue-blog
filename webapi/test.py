# -*- coding: UTF-8 -*-
import asyncio
from sqlalchemy import update, func, delete, and_
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from webapi.db.dals.category_dal import Category
from webapi.db.dals.post_dal import PostDAL, Post
from webapi.db.config import async_session


async def t_func():
    async with async_session() as session:
        async with session.begin():
            # post_dal = PostDAL(session)
            # result = await post_dal.count()
            # print(result)
            # stmt = select(func.count(Post.id).label('total'))
            # if title is not None:
            #     stmt = stmt.where(Post.title.like(f'%{title}%'))
            # if is_published is not None:
            #     stmt = stmt.where(Post.is_published == is_published)
            # if category_id is not None:
            # q = await self.db_session.execute(stmt)
            # return q.one()['total']
            stmt = select(Post).options(selectinload(Post.categories), selectinload(Post.comments))
            stmt = stmt.where(Post.categories.any(Category.id == 1))
            print(stmt)
            q = await session.execute(stmt)
            result = q.scalars().all()
            print(result)
            # print(result[0].categories)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(t_func())
