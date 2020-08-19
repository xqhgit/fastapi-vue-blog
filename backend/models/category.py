from datetime import datetime
from sqlalchemy import Integer, Column, String, LargeBinary
from sqlalchemy.orm import relationship

from backend.db.base import Base


class Category(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    image = Column(LargeBinary)
    timestamp = Column(Integer, default=lambda: int(datetime.timestamp(datetime.utcnow())), index=True)

    posts = relationship('Post', back_populates='category')
