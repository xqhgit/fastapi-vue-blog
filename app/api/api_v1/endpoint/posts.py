# coding=utf8
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.api import deps
from app import schemas, crud

router = APIRouter()


@router.get('/', response_model=schemas.PostsOut, status_code=status.HTTP_200_OK)
def get_posts(
        db: Session = Depends(deps.get_db),
        limit: int = 10,
        page: int = 1
):
    total = crud.post.count(db)
    items = crud.post.get_multi(db)
    return {'total': total, 'items': items}


# @router.get('/list')


@router.post('/', status_code=status.HTTP_201_CREATED
             # dependencies=[Depends(deps.get_current_active_admin), ]
             )
def create_post(
        db: Session = Depends(deps.get_db),
        *,
        obj_in: schemas.PostCreate
):
    crud.post.create(db, obj_in=obj_in)
    return JSONResponse(content={'msg': '创建成功'}, status_code=status.HTTP_201_CREATED)


@router.get('/list', response_model=schemas.PostListOut, status_code=status.HTTP_200_OK,
            # dependencies=[Depends(deps.get_current_active_admin), ]
            )
def get_posts_list(
        db: Session = Depends(deps.get_db)
):
    total = crud.post.count(db)
    items = crud.post.get_list(db)
    print(items)
    return {'total': total, 'items': items}

