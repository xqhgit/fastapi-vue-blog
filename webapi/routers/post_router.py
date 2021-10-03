# -*-coding:utf-8 -*-
from typing import List, Optional

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from webapi.db.dals.post_dal import Post, PostDAL
from webapi.utils.dependencies import DALGetter, get_current_user
from webapi.db.schemas.post import PostsListOut, PostOut, PostIn, PostOutCreate

router = APIRouter()


@router.get("/", tags=['Post'], status_code=status.HTTP_200_OK, response_model=PostsListOut)
async def get_posts(
        dal: PostDAL = Depends(DALGetter(PostDAL)),
        page: int = 1, limit: int = 10, title: str = None
):
    total = await dal.count(title)
    items = await dal.get_limit(title, page=page, limit=limit)
    result = {'total': total, 'items': items}
    return result


@router.post('/', tags=['Post'], dependencies=[Depends(get_current_user), ],
             response_model=PostOutCreate, status_code=status.HTTP_201_CREATED)
async def create_post(
        dal: PostDAL = Depends(DALGetter(PostDAL)), *,
        obj_in: PostIn
):
    exist = await dal.get_by_title(obj_in.title)
    if exist:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'detail': '标题已存在'})
    return await dal.create(obj_in)


@router.get('/{post_id}/', tags=['Post'], status_code=status.HTTP_200_OK, response_model=PostOut)
async def get_post(
        dal: PostDAL = Depends(DALGetter(PostDAL)), *,
        post_id: int
):
    obj = await dal.get_by_id(post_id)
    return obj
