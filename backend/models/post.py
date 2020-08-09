from sqlalchemy import Integer, Column, String, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.db.base import Base


class Post(Base):
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=lambda: int(datetime.timestamp(datetime.utcnow())), index=True)
    title = Column(String(60))
    body = Column(Text)
    can_comment = Column(Boolean, default=True)

    category_id = Column(Integer, ForeignKey('category.id'))

    category = relationship('Category', back_populates='posts')
    comments = relationship('Comment', back_populates='post', cascade='all, delete-orphan')

