# coding=utf8
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder

from app import crud, schemas
from app.api import deps

# from app.schemas import CategoryCreate, CategoryOut, CategoryItems

router = APIRouter()


@router.get('/', response_model=schemas.CategoryItems, status_code=status.HTTP_200_OK)
def get_categories(
        db: Session = Depends(deps.get_db)
):
    items = crud.category.get_list(db)
    result = {
        'total': len(items),
        'items': items
    }
    return jsonable_encoder(result)


@router.post('/', response_model=schemas.CategoryCreateOut, status_code=status.HTTP_201_CREATED,
             # dependencies=[Depends(deps.get_current_active_admin), ]
             )
def create_category(
        db: Session = Depends(deps.get_db),
        *,
        obj_in: schemas.CategoryCreate
):
    db_obj = crud.category.create(db, obj_in=obj_in)
    return db_obj


@router.get('/select_list', response_model=schemas.CategorySelectListOut, status_code=status.HTTP_200_OK,
            # dependencies=[Depends(deps.get_current_active_admin), ]
            )
def get_categories_select(db: Session = Depends(deps.get_db)):
    items = crud.category.get_select_list(db)
    return {'items': items}
