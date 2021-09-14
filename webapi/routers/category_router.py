from typing import List, Optional

from fastapi import APIRouter, Depends, status

from webapi.db.dals.category_dal import CategoryDAL, Category
from webapi.utils.dependencies import DALGetter
from webapi.db.schemas.category import CategoryCreate, CategoryOut

router = APIRouter()


@router.get("/", tags=['Category'])
async def get_all_categories(dal: CategoryDAL = Depends(DALGetter(CategoryDAL))) -> List[Category]:
    return await dal.get_all()


# TODO: Admin Auth
@router.post('/', tags=['Category'],
             response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
async def create_category(
        category_schema: CategoryCreate,
        dal: CategoryDAL = Depends(DALGetter(CategoryDAL)),
):
    db_obj = await dal.create(category_schema)
    return db_obj
