from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from backend import crud, schemas
from backend.utils import utils
from backend.api import deps

router = APIRouter()


@router.get('/')
def read_posts(
        limit: int = 10,
        page: int = 1
):
    offset = limit * (page - 1)
    images = [
        '1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg'
    ]
    items = []
    x = 1
    for image in images:
        items.append({
            'image': utils.img_base64(image),
            'id': x
        })
        x += 1
    total = len(items)
    items = items[offset:offset + limit]
    result = {
        "total": total,
        "items": items
    }
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@router.post('/', dependencies=[Depends(deps.get_current_active_admin)], status_code=status.HTTP_201_CREATED)
def create_post(
        db: Session = Depends(deps.get_db),
        *, post_in: schemas.PostCreate
):
    try:
        post = crud.post.create(db, obj_in=post_in)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Parameter error"
        )
    return
