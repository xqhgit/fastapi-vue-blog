from typing import List, Optional
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from webapi.db.dals.user_dal import User, UserDAL
from webapi.db.schemas.token import Token
from webapi.utils.dependencies import DALGetter, get_current_user
from webapi.setting import settings
from webapi.utils import security

router = APIRouter()


@router.post("/login/access_token/", tags=['User'],
             response_model=Token, status_code=status.HTTP_201_CREATED)
async def login_access_token(
        dal: UserDAL = Depends(DALGetter(UserDAL)),
        form_data: OAuth2PasswordRequestForm = Depends()
):
    user = await dal.authenticate(
        username=form_data.username,
        password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect email or password"
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        'access_token': security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer"
    }


@router.get('/login/getinfo/', tags=['User'])
async def login_getinfo(
        current_user: User = Depends(get_current_user)
):
    data = {
        'username': current_user.username,
        'nickname': current_user.nickname,
        'roles': ['admin', ]
    }
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)
