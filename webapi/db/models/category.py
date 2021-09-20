from sqlalchemy import Text, Integer, Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from webapi.db.config import Base
from webapi.db.models.m2m import post_category


class Category(Base):
    __tablename__ = 'Category'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True)
    posts = relationship('Post', back_populates='categories', secondary=post_category)
