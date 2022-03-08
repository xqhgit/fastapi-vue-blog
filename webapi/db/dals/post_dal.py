from typing import List, Optional
from fastapi import status
from fastapi.exceptions import HTTPException


from sqlalchemy import update, func, delete, and_, desc
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload, with_loader_criteria

from webapi.db.models import Post, Category, Comment, post_category
from webapi.db.schemas.post import PostIn, PostInUpdate
from webapi.utils.elastic import es_update_doc, es_delete_doc, es_create_doc


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
        if db_obj.is_published:
            await es_create_doc({
                'id': db_obj.id,
                'title': db_obj.title,
                'description': db_obj.description,
                'body': db_obj.body,
                'timestamp': db_obj.timestamp,
            })
        return db_obj

    async def update(self, db_obj: Post, obj_in: PostInUpdate):
        update_data = obj_in.dict(exclude_none=True)
        category_ids = update_data.get('categories', None)
        if category_ids is not None:
            categories = await self.get_categories_by_ids(category_ids)
            update_data['categories'] = categories

        for field in update_data:
            setattr(db_obj, field, update_data[field])
        self.db_session.add(db_obj)
        await self.db_session.flush()
        # 如果不发布，则删除查询文本
        if db_obj.is_published:
            await es_update_doc({
                'id': db_obj.id,
                'title': db_obj.title,
                'description': db_obj.description,
                'body': db_obj.body,
                'timestamp': db_obj.timestamp,
            })
        else:
            await es_delete_doc(db_obj.id)
        return db_obj

    async def delete(self, *, db_obj: Post):
        db_obj.categories = []
        await self.db_session.flush()
        await self.db_session.execute(delete(Post).where(Post.id == db_obj.id))
        await es_delete_doc(db_obj.id)

    async def count(self, title=None, is_published=None, category_id=None):
        stmt = select(func.count(Post.id).label('total'))
        if title is not None:
            stmt = stmt.where(Post.title.like(f'%{title}%'))
        if is_published is not None:
            stmt = stmt.where(Post.is_published == is_published)
        if category_id is not None:
            stmt = stmt.where(Post.categories.any(Category.id == category_id))
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

    async def get_by_id(self, record_id: int, is_published=None, can_comment=None, reviewed=None):
        stmt = select(Post).options(selectinload(Post.categories), selectinload(Post.comments)).where(
            Post.id == record_id)
        if is_published is not None:
            stmt = stmt.where(Post.is_published == is_published)
        if can_comment is not None:
            stmt = stmt.where(Post.can_comment == can_comment)
        if reviewed is not None:
            # TODO: 如果父评论被切回未审核，序列化将会报错
            stmt = stmt.options(
                with_loader_criteria(Comment, Comment.reviewed == reviewed)
            )
        q = await self.db_session.execute(stmt)
        result = q.scalars().all()
        if result:
            return result[0]
        else:
            return None

    async def get_limit(self, title=None, *, page, limit, is_published=None, category_id=None) -> List[Post]:
        offset = limit * (page - 1)
        stmt = select(Post).options(selectinload(Post.categories), selectinload(Post.comments))
        if title is not None:
            stmt = stmt.where(Post.title.like(f'%{title}%'))
        if is_published is not None:
            stmt = stmt.where(Post.is_published == is_published)
        if category_id is not None:
            stmt = stmt.where(Post.categories.any(Category.id == category_id))
        stmt = stmt.order_by(desc(Post.timestamp)).offset(offset).limit(limit)
        q = await self.db_session.execute(stmt)
        return q.scalars().all()

    async def update_elastic_doc(self):
        pass

    async def delete_elastic_doc(self):
        pass
