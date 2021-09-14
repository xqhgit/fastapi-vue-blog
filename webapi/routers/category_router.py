from typing import List, Optional

from fastapi import APIRouter, Depends, status

from webapi.db.dals.category_dal import CategoryDAL, Category
from webapi.utils.dependencies import DALGetter, get_current_user
from webapi.db.schemas.category import CategoryCreate, CategoryOut, CategoryAllOut, CategorySelectionOut

router = APIRouter()


@router.get("/", tags=['Category'], response_model=CategoryAllOut, status_code=status.HTTP_200_OK)
async def get_all_categories(dal: CategoryDAL = Depends(DALGetter(CategoryDAL))) -> List[Category]:
    return await dal.get_all()


@router.post('/', tags=['Category'], dependencies=[Depends(get_current_user), ],
             response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
async def create_category(
        category_schema: CategoryCreate,
        dal: CategoryDAL = Depends(DALGetter(CategoryDAL)),
):
    return await dal.create(category_schema)


@router.get('/selection/', tags=['Category'], response_model=CategorySelectionOut, status_code=status.HTTP_200_OK)
async def get_selection_categories(dal: CategoryDAL = Depends(DALGetter(CategoryDAL))):
    return await dal.get_selection()
