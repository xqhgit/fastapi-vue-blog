from fastapi import Depends, HTTPException, status, Header
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from jose import jwt

from webapi.db.config import async_session
from webapi.db import models, schemas
from webapi.db.dals.user_dal import UserDAL
from webapi.setting import settings
from webapi.utils import security


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f'/api/admin/login/access_token/'
)


class DALGetter:
    def __init__(self, dal_cls):
        self.dal_cls = dal_cls

    async def __call__(self):
        async with async_session() as session:
            async with session.begin():
                yield self.dal_cls(session)


async def get_current_user(
        dal: UserDAL = Depends(DALGetter(UserDAL)), token: str = Depends(reusable_oauth2)
) -> models.User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.token.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise credentials_exception
    user = await dal.get(id=token_data.sub)
    if user is None:
        raise credentials_exception
    return user
