# -*-coding:utf-8 -*-

from typing import List, Optional

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from webapi.db.models.user import User
from webapi.db.dals.post_dal import Post, PostDAL
from webapi.db.dals.comment_dal import Comment, CommentDAL
from webapi.utils.dependencies import DALGetter, get_current_user
from webapi.db.schemas.comment import CommentCreateAdmin, CommentCreateAnonymous, CommentCreate

router = APIRouter()


@router.post('/', tags=['Comment'], status_code=status.HTTP_201_CREATED)
async def create_comment(
        user: User = Depends(get_current_user),
        comment_dal: CommentDAL = Depends(DALGetter(CommentDAL)),
        post_dal: PostDAL = Depends(DALGetter(PostDAL)), *,
        obj_in: CommentCreateAdmin
):
    post_obj = await post_dal.get_by_id(obj_in.post_id)
    if not post_obj:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'detail': '文章不存在'})
    comment_schema = CommentCreate(
        **obj_in.dict(),
        author=user.nickname,
        email=user.email,
        from_admin=True,
        reviewed=True
    )
    await comment_dal.create(obj_in=comment_schema)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={'detail': 'OK'})


@router.post('/anonymous/', tags=['Comment'], status_code=status.HTTP_201_CREATED)
async def create_comment_anonymous(
        comment_dal: CommentDAL = Depends(DALGetter(CommentDAL)),
        post_dal: PostDAL = Depends(DALGetter(PostDAL)), *,
        obj_in: CommentCreateAnonymous
):
    post_obj = await post_dal.get_by_id(obj_in.post_id)
    if not post_obj:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'detail': '文章不存在'})
    comment_schema = CommentCreate(
        **obj_in.dict(),
        from_admin=False,
        reviewed=False
    )
    await comment_dal.create(obj_in=comment_schema)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={'detail': 'OK'})
