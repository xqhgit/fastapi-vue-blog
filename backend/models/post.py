from sqlalchemy import Integer, Column, String, DateTime, Text, Boolean, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.db.base import Base


class Post(Base):
    id = Column(Integer, primary_key=True)
    timestamp = Column(Integer, default=lambda: int(datetime.timestamp(datetime.utcnow())), index=True)
    title = Column(String(60))
    summary = Column(Text)
    content = Column(Text)
    is_publish = Column(Boolean, default=False)
    can_comment = Column(Boolean, default=True)
    cover_image = Column(LargeBinary)

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='posts')
    comments = relationship('Comment', back_populates='post', cascade='all, delete-orphan')
    attachments = relationship('Attachment', secondary='t_post_attachment', lazy='dynamic')

