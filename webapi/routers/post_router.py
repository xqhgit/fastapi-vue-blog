from typing import List, Optional

from fastapi import APIRouter, Depends

from webapi.db.dals.post_dal import Post, PostDAL
from webapi.utils.dependencies import DALGetter

router = APIRouter()


@router.get("/posts",  tags=['Post'])
async def get_all_posts(dal: PostDAL = Depends(DALGetter(PostDAL))) -> List[Post]:
    return await dal.get_all_posts()

