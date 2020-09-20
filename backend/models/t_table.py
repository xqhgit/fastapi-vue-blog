from sqlalchemy import Column, Table, ForeignKey, Integer

from backend.db.base import Base


t_post_attachment = Table(
    't_post_attachment',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('post.id')),
    Column('attachment_id', Integer, ForeignKey('attachment.id'))
)


t_category_attachment = Table(
    't_category_attachment',
    Base.metadata,
    Column('category_id', Integer, ForeignKey('category.id')),
    Column('attachment_id', Integer, ForeignKey('attachment.id'))
)
