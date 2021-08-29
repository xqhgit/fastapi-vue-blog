from datetime import datetime

from sqlalchemy import Text, Integer, Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from webapi.db.config import Base


class Post(Base):
    __tablename__ = 'Post'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), unique=True)
    description = Column(Text)
    body = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    can_comment = Column(Boolean, default=True)
    is_published = Column(Boolean, default=True)

    category_id = Column(Integer, ForeignKey('Category.id'))

    category = relationship('Category', back_populates='posts')
    comments = relationship('Comment', back_populates='post', cascade='all, delete-orphan')
