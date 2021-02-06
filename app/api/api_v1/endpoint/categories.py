# coding=utf8
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.api import deps

router = APIRouter()


@router.get('/')
def get_categories(
        db: Session = Depends(deps.get_db),
):
    pass


