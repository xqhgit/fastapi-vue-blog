from datetime import datetime

from sqlalchemy import Text, Integer, Column, String, DateTime, Boolean, ForeignKey, func, and_
from sqlalchemy.orm import relationship

from webapi.db.config import Base
from webapi.db.models.m2m import post_category
from webapi.db.models import Comment


class Post(Base):
    __tablename__ = 'Post'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64))
    description = Column(Text)
    body = Column(Text)
    body_html = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    can_comment = Column(Boolean, default=True)
    is_published = Column(Boolean, default=True)

    comments = relationship('Comment', back_populates='post', cascade='all, delete-orphan')
    categories = relationship('Category', back_populates='posts', secondary=lambda: post_category)

    __mapper_args__ = {"eager_defaults": True}
