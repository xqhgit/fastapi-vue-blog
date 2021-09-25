from typing import List, Optional

from fastapi import APIRouter, Depends, status
from fastapi.responses import Response

from webapi.db.dals.post_dal import Post, PostDAL
from webapi.utils.dependencies import DALGetter
from webapi.db.schemas.post import PostsListOut, PostOut

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


@router.get('/{post_id}/', tags=['Post'], status_code=status.HTTP_200_OK, response_model=PostOut)
async def get_post(
        dal: PostDAL = Depends(DALGetter(PostDAL)), *,
        post_id: int
):
    obj = await dal.get_by_id(post_id)
    return obj
