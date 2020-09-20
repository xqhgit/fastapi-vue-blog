from sqlalchemy import LargeBinary, Integer, Column, String
from sqlalchemy.orm import relationship

from backend.db.base import Base


class Attachment(Base):

    id = Column(Integer, primary_key=True)
    uid = Column(String(255), unique=True)
    filename = Column(String(255))
    content_type = Column(String(32))
    url = Column(String(255))

    posts = relationship('Post', secondary='t_post_attachment', lazy='dynamic')

