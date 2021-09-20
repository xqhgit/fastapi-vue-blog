# -*-coding:utf-8 -*-

from typing import List, Optional

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from webapi.db.dals.category_dal import CategoryDAL, Category
from webapi.utils.dependencies import DALGetter, get_current_user
from webapi.db.schemas.category import CategoryCreate, CategoryOut, CategoryAllOut, CategorySelectionOut, CategoryUpdate

router = APIRouter()


@router.get("/", tags=['Category'], response_model=CategoryAllOut, status_code=status.HTTP_200_OK)
async def get_all_categories(
        dal: CategoryDAL = Depends(DALGetter(CategoryDAL)),
        unlimit: bool = True, page: int = 1, limit: int = 10, *, name: str = None
):
    total = await dal.count(name=name)
    if unlimit:
        result = await dal.get_all(name=name)
    else:
        result = await dal.get_limit(page=page, limit=limit, name=name)
    return {'total': total, 'items': result}


@router.post('/', tags=['Category'], dependencies=[Depends(get_current_user), ],
             response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
async def create_category(
        category_schema: CategoryCreate,
        dal: CategoryDAL = Depends(DALGetter(CategoryDAL)),
):
    exist = await dal.get_by_name(category_schema.name)
    if exist:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'detail': '类别已存在'})
    return await dal.create(category_schema)


@router.get('/selection/', tags=['Category'], response_model=CategorySelectionOut, status_code=status.HTTP_200_OK)
async def get_selection_categories(dal: CategoryDAL = Depends(DALGetter(CategoryDAL))):
    return await dal.get_selection()


@router.put('/{category_id}/', tags=['Category'], dependencies=[Depends(get_current_user), ],
            response_model=CategoryOut, status_code=status.HTTP_200_OK)
async def create_category(
        category_id: int,
        category_schema: CategoryUpdate,
        dal: CategoryDAL = Depends(DALGetter(CategoryDAL)),
):
    obj = await dal.get_by_id(category_id)
    if not obj:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'detail': '类别不存在'})
    db_obj = await dal.update(db_obj=obj, obj_in=category_schema)
    return db_obj
