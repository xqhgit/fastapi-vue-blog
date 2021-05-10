# coding=utf8
import hashlib
import bleach
from markdown import markdown
from datetime import datetime
from sqlalchemy import Text, Integer, Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.event import listen, listens_for

from app.db.base import Base


class Admin(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(64), unique=True, index=True)
    username = Column(String(64), unique=True, index=True)
    password_hash = Column(String(128))
    name = Column(String(64))
    avatar_hash = Column(String(32))
    about_me = Column(Text)

    def gravatar_hash(self):
        return hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()

    def gravatar(self, size=100, default='identicon', rating='g'):
        url = 'https://secure.gravatar.com/avatar'
        hash = self.avatar_hash or self.gravatar_hash()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
            url=url, hash=hash, size=size, default=default, rating=rating)


class Category(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    posts = relationship('Post', back_populates='category')


class Post(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    body = Column(Text)
    body_html = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    can_comment = Column(Boolean, default=True)

    category_id = Column(Integer, ForeignKey('category.id'))

    category = relationship('Category', back_populates='posts')
    comments = relationship('Comment', back_populates='post', cascade='all, delete-orphan')

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True))


class Comment(Base):
    id = Column(Integer, primary_key=True)
    author = Column(String(64))
    email = Column(String(254))
    body = Column(Text)
    body_html = Column(Text)
    # from_admin = Column(Boolean, default=False)  # 用于判断是否为管理员的评论
    # reviewed = Column(Boolean, default=False)  # 用于判断评论是否通过审核
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)

    replied_id = Column(Integer, ForeignKey('comment.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    post = relationship('Post', back_populates='comments')
    replies = relationship('Comment', back_populates='replied', cascade='all, delete-orphan')
    replied = relationship('Comment', back_populates='replies', remote_side=[id])

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'code', 'em', 'i',
                        'strong']
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True))


# listen(Post.body, 'set', Post.on_changed_body)
# listen(Comment.body, 'set', Comment.on_changed_body)
