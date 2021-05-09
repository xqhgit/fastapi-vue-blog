# coding=utf8
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from app.api import deps
from app import schemas, crud

router = APIRouter()


@router.get('/')
def get_posts(
        db: Session = Depends(deps.get_db),
        limit: int = 10,
        page: int = 1
):
    pass


# @router.get('/list')


@router.post('/', response_model=schemas.PostCreateOut, status_code=status.HTTP_201_CREATED,
             # dependencies=[Depends(deps.get_current_active_admin), ]
             )
def create_post(
        db: Session = Depends(deps.get_db),
        *,
        obj_in: schemas.PostCreate
):
    # print(obj_in.dict())
    db_obj = crud.post.create(db, obj_in=obj_in)
    return db_obj
