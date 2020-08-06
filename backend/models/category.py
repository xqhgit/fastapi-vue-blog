from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from backend.db.base import Base


class Category(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)

    posts = relationship('Post', back_populates='category')
