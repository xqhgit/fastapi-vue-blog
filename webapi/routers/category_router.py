from typing import List, Optional

from fastapi import APIRouter, Depends

from webapi.db.dals.category_dal import CategoryDAL
from webapi.db.models.category import Category
from webapi.utils.dependencies import DALGetter

router = APIRouter()


@router.get("/books")
async def get_all_books(category_dal: CategoryDAL = Depends(DALGetter(Category))) -> List[Category]:
    return await category_dal.get_all_categories()

