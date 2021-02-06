# coding=utf8
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.api import deps

router = APIRouter()


@router.get('/')
def get_posts(
        db: Session = Depends(deps.get_db),
        limit: int = 10,
        page: int = 1
):
    pass
