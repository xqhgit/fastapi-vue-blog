from typing import List, Optional

from fastapi import APIRouter, Depends

from webapi.db.dals.category_dal import CategoryDAL, Category
from webapi.utils.dependencies import DALGetter

router = APIRouter()


@router.get("/categories",  tags=['Category'])
async def get_all_categories(dal: CategoryDAL = Depends(DALGetter(CategoryDAL))) -> List[Category]:
    return await dal.get_all_categories()


@router.post('/categories', tags=['Category'])
async def create_category(dal: CategoryDAL = Depends(DALGetter(CategoryDAL))):
    pass

