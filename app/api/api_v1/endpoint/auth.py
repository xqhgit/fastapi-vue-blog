from typing import Any
from datetime import timedelta
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from app import schemas, crud, models
from app.api import deps
from app.core.config import settings
from app.core import security

router = APIRouter()


@router.post('/login/access-token', response_model=schemas.Token, status_code=status.HTTP_201_CREATED)
def login_access_token(
        db: Session = Depends(deps.get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """OAuth2 compatible token login, get an access token for future requests"""
    admin = crud.admin.authenticate(
        db=db,
        username=form_data.username,
        password=form_data.password
    )
    if not admin:
        raise HTTPException(
            status_code=400, detail="Incorrect email or password"
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        'access_token': security.create_access_token(
            admin.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer"
    }


@router.get('/login/info')
def login_info(
        current_user: models.Admin = Depends(deps.get_current_active_admin),
):
    data = {
        "name": current_user.username,
        "roles": ['admin']
    }
    return JSONResponse(content=jsonable_encoder(data), status_code=status.HTTP_200_OK)

