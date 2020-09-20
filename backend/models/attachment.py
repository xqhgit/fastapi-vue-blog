from sqlalchemy import LargeBinary, Integer, Column, String
from backend.db.base import Base


class Attachment(Base):

    id = Column(Integer, primary_key=True)
    uid = Column(String(255), unique=True)
    filename = Column(String(255))
    suffix = Column(String(8))
    url = Column(String(255))

