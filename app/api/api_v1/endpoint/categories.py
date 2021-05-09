# coding=utf8
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder

from app import crud
from app.api import deps
from app.schemas import CategoryCreate, CategoryOut, CategoryItems

router = APIRouter()


@router.get('/', response_model=CategoryItems, status_code=status.HTTP_200_OK)
def get_categories(
        db: Session = Depends(deps.get_db)
):
    items = crud.category.get_list(db)
    result = {
        'total': len(items),
        'items': items
    }
    return jsonable_encoder(result)




