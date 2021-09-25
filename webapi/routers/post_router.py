from typing import List, Optional

from fastapi import APIRouter, Depends, status
from fastapi.responses import Response

from webapi.db.dals.post_dal import Post, PostDAL
from webapi.utils.dependencies import DALGetter
from webapi.db.schemas.post import PostsListOut

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
