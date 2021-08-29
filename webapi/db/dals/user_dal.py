from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from webapi.db.models import User


class UserDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def authenticate(self, *, username, password):
        user = await self.db_session.execute(select(User).where(User.username == username))
        if not user:
            return None
        if not user.verify_password(password, user.password_hash):
            return None
        return user

