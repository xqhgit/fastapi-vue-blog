from typing import Union, Any
from datetime import datetime, timedelta

import jwt
from sqlalchemy import Text, Integer, Column, String, DateTime, Boolean, ForeignKey
from passlib.context import CryptContext

from webapi.db.config import Base


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
ALGORITHM = 'HS256'


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, index=True)
    password_hash = Column(String(255))
    nickname = Column(String(64), unique=True, index=True)
    email = Column(String(64), unique=True, index=True)
    about_me = Column(Text)

    # generate hash password
    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)

    # verify login password
    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        return pwd_context.verify(password, hashed_password)

    # generate access token
    @staticmethod
    def create_access_token(
            subject: Union[str, Any], expires_delta: timedelta = None
    ) -> str:
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        to_encode = {
            'exp': expire,
            'sub': str(subject)
        }
        encoded_jwt = jwt.encode(
            to_encode, settings.SECRET_KEY, algorithm=ALGORITHM
        )
        return encoded_jwt


