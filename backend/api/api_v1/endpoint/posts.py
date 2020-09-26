import base64

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, Form, UploadFile, File
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from backend import crud, schemas
from backend.utils import utils
from backend.api import deps

router = APIRouter()


@router.get('/')
def read_posts(
        db: Session = Depends(deps.get_db),
        limit: int = 10,
        page: int = 1
):
    posts = crud.post.get_multi(db, limit=limit, page=page)
    result = {
        'total': len(posts),
        'items': [p._asdict() for p in posts]
    }
    return JSONResponse(
        content=jsonable_encoder(result), status_code=status.HTTP_200_OK
    )


@router.post('/', dependencies=[Depends(deps.get_current_active_admin)], status_code=status.HTTP_201_CREATED)
def create_post(
        db: Session = Depends(deps.get_db), *,
        title: str = Form(...), is_publish: bool = Form(...),
        can_comment: bool = Form(...), category_id: int = Form(...),
        cover_image: UploadFile = File(...), content: str = Form(...)
        # *, post_in: schemas.PostCreate
):
    obj_in = schemas.PostCreate(
        title=title,
        is_publish=is_publish,
        can_comment=can_comment,
        category_id=category_id,
        cover_image=base64.b64encode(cover_image.file.read()),
        content=content
    )
    try:
        post = crud.post.create(db, obj_in=obj_in)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Parameter error"
        )
    return JSONResponse(content='ok', status_code=status.HTTP_201_CREATED)


@router.get('/manage', dependencies=[Depends(deps.get_current_active_admin)])
def manage_read_posts(
        db: Session = Depends(deps.get_db),
        limit: int = 10,
        page: int = 1
):
    pass
