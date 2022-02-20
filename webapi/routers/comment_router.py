# -*-coding:utf-8 -*-
from fastapi import APIRouter, Depends, status, BackgroundTasks
from fastapi.responses import JSONResponse

from webapi.db.models.user import User
from webapi.db.dals.post_dal import Post, PostDAL
from webapi.db.dals.comment_dal import Comment, CommentDAL
from webapi.utils.dependencies import DALGetter, get_current_user
from webapi.db.schemas.comment import (
    CommentCreateAdmin, CommentCreateAnonymous, CommentCreate,
    CommentsListOut, CommentInUpdate
)

router = APIRouter()


@router.get('/', tags=['Comment'], dependencies=[Depends(get_current_user), ],
            status_code=status.HTTP_200_OK, response_model=CommentsListOut)
async def get_comments(
        dal: CommentDAL = Depends(DALGetter(CommentDAL)),
        page: int = 1, limit: int = 10, reviewed: bool = None
):
    total = await dal.count(reviewed=reviewed)
    items = await dal.get_limit(reviewed=reviewed, page=page, limit=limit)
    result = {'total': total, 'items': items}
    return result


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
    post_obj = await post_dal.get_by_id(obj_in.post_id, can_comment=True)
    if not post_obj:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'detail': '文章不存在'})
    comment_schema = CommentCreate(
        **obj_in.dict(),
        from_admin=False,
        reviewed=False
    )
    await comment_dal.create(obj_in=comment_schema)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={'detail': 'OK'})


@router.put('/{comment_id}/', tags=['Comment'], dependencies=[Depends(get_current_user), ],
            status_code=status.HTTP_200_OK)
async def update_comment(
        dal: CommentDAL = Depends(DALGetter(CommentDAL)), *,
        comment_id: int, obj_in: CommentInUpdate
):
    obj = await dal.get_by_id(comment_id)
    if not obj:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'detail': '文章不存在'})
    db_obj = await dal.update(db_obj=obj, obj_in=obj_in)
    return db_obj


@router.delete('/{comment_id}/', tags=['Comment'], dependencies=[Depends(get_current_user), ],
               status_code=status.HTTP_200_OK)
async def delete_comment(
        dal: CommentDAL = Depends(DALGetter(CommentDAL)), *,
        comment_id: int
):
    obj = await dal.get_by_id(comment_id)
    if not obj:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'detail': '评论不存在'})
    await dal.delete(db_obj=obj)
    return JSONResponse(status_code=status.HTTP_200_OK, content={'detail': 'OK'})
