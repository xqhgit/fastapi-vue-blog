import datetime

from sqlalchemy import Text, Integer, Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from webapi.db.config import Base


class Comment(Base):
    __tablename__ = 'Comment'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.now, index=True)
    from_admin = Column(Boolean, default=False)  # 用于判断是否为管理员的评论
    reviewed = Column(Boolean, default=False)  # 用于判断评论是否通过审核

    author = Column(String(30))
    email = Column(String(254))
    body = Column(Text)

    replied_id = Column(Integer, ForeignKey('Comment.id'))
    post_id = Column(Integer, ForeignKey('Post.id'))

    post = relationship('Post', back_populates='comments')
    replies = relationship('Comment', back_populates='replied', cascade='all, delete-orphan')
    replied = relationship('Comment', back_populates='replies', remote_side=[id])

