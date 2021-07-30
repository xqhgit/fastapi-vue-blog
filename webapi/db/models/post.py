from datetime import datetime

from sqlalchemy import Text, Integer, Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from webapi.db.config import Base


class Post(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(64), unique=True)
    description = Column(Text)
    body = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    can_comment = Column(Boolean, default=True)

    category_id = Column(Integer, ForeignKey('category.id'))

    category = relationship('Category', back_populates='posts')
    comments = relationship('Comment', back_populates='post', cascade='all, delete-orphan')
