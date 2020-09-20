import base64
from typing import Union, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, Body, UploadFile, File, Form
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from backend import crud, schemas
from backend.utils import utils
from backend.api import deps

router = APIRouter()


@router.get('/', response_model=schemas.CategoryItems, status_code=status.HTTP_200_OK)
def read_categories(
        db: Session = Depends(deps.get_db), *,
        page: int = 1, limit: int = 10
):
    total = crud.category.count(db)
    categories = crud.category.get_multi(db, page=page, limit=limit)
    result = {
        'total': total,
        'items': categories
    }
    return result


@router.post('/',
             dependencies=[Depends(deps.get_current_active_admin)],
             response_model=schemas.CategoryOut, status_code=status.HTTP_201_CREATED)
def create_category(
        db: Session = Depends(deps.get_db), img: UploadFile = File(...), name: str = Form(...)
        # *, category_in: schemas.CategoryCreate
):
    category_in = schemas.CategoryCreate(
        name=name, image=base64.b64encode(img.file.read())
    )
    category = crud.category.create(db, obj_in=category_in)
    return JSONResponse(content={}, status_code=status.HTTP_201_CREATED)


@router.get('/options', dependencies=[Depends(deps.get_current_active_admin)],
            status_code=status.HTTP_200_OK)
def read_categories_options(
        db: Session = Depends(deps.get_db)
):
    data = crud.category.get_options(db)
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)


@router.delete('/{category_id}', dependencies=[Depends(deps.get_current_active_admin)],
               status_code=status.HTTP_200_OK)
def delete_category(
        db: Session = Depends(deps.get_db),
        *, category_id: int
):
    crud.category.delete(db, ids=[category_id, ])
    return JSONResponse(content='ok', status_code=status.HTTP_201_CREATED)


@router.put('/{category_id}', dependencies=[Depends(deps.get_current_active_admin)], response_model=schemas.CategoryOut,
            status_code=status.HTTP_200_OK)
def update_category(
        db: Session = Depends(deps.get_db),
        *, category_id: int, category_in: schemas.CategoryUpdate
):
    category = crud.category.get(db, id=category_id)
    if not category:
        raise HTTPException(
            status_code=404,
            detail="Not Found.",
        )
    category = crud.category.update(db, db_obj=category, obj_in=category_in)
    return category


@router.get('/{category_id}', response_model=schemas.CategoryOut, status_code=status.HTTP_200_OK)
def read_category(
        db: Session = Depends(deps.get_db),
        *, category_id: int
):
    category = crud.category.get(db, id=category_id)
    if not category:
        raise HTTPException(
            status_code=404,
            detail="Not Found.",
        )
    return category
