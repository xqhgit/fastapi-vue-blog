# -*-coding:utf-8 -*-
from typing import List, Optional

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from webapi.db.dals.post_dal import Post, PostDAL
from webapi.utils.dependencies import DALGetter, get_current_user
from webapi.db.schemas.post import PostsListOut, PostOut, PostIn, PostOutCreate, PostInUpdate, PostOutUpdate, PostsSearchListOut
from webapi.utils.elastic import es_search

router = APIRouter()


@router.get("/", tags=['Post'], dependencies=[Depends(get_current_user), ],
            status_code=status.HTTP_200_OK, response_model=PostsListOut)
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
    return await dal.create(obj_in)


@router.get("/published/", tags=['Post'], status_code=status.HTTP_200_OK, response_model=PostsListOut)
async def get_posts_published(
        dal: PostDAL = Depends(DALGetter(PostDAL)),
        page: int = 1, title: str = None, category_id: int = None
):
    total = await dal.count(title, is_published=True, category_id=category_id)
    items = await dal.get_limit(title, page=page, limit=10, is_published=True, category_id=category_id)
    result = {'total': total, 'items': items}
    return result


@router.get('/published/search/', tags=['Post'], status_code=status.HTTP_200_OK, response_model=PostsSearchListOut)
async def search_posts_published(
        keyword: str,
        page: int = 1
):
    data = await es_search(keyword, page)
    return data


@router.get('/published/{post_id}/', tags=['Post'], status_code=status.HTTP_200_OK, response_model=PostOut)
async def get_post_published(
        dal: PostDAL = Depends(DALGetter(PostDAL)), *,
        post_id: int
):
    obj = await dal.get_by_id(post_id, is_published=True, reviewed=True)
    return obj


@router.get('/{post_id}/', tags=['Post'], dependencies=[Depends(get_current_user), ],
            status_code=status.HTTP_200_OK, response_model=PostOut)
async def get_post(
        dal: PostDAL = Depends(DALGetter(PostDAL)), *,
        post_id: int
):
    obj = await dal.get_by_id(post_id)
    return obj


@router.put('/{post_id}/', tags=['Post'], dependencies=[Depends(get_current_user), ],
            status_code=status.HTTP_200_OK, response_model=PostOutUpdate)
async def update_post(
        dal: PostDAL = Depends(DALGetter(PostDAL)), *,
        post_id: int, obj_in: PostInUpdate
):
    obj = await dal.get_by_id(post_id)
    if not obj:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'detail': '文章不存在'})
    db_obj = await dal.update(db_obj=obj, obj_in=obj_in)
    return db_obj


@router.delete('/{post_id}/', tags=['Post'], dependencies=[Depends(get_current_user), ],
               status_code=status.HTTP_200_OK)
async def delete_post(
        dal: PostDAL = Depends(DALGetter(PostDAL)), *,
        post_id: int
):
    obj = await dal.get_by_id(post_id)
    if not obj:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'detail': '文章不存在'})
    await dal.delete(db_obj=obj)
    return JSONResponse(status_code=status.HTTP_200_OK, content={'detail': 'OK'})
