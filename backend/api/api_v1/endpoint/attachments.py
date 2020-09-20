import uuid
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.requests import Request

from backend.api import deps
from backend import crud


router = APIRouter()
# router.url_path_for()


@router.post('/', dependencies=[Depends(deps.get_current_active_admin), ])
def create_attachment(
        db: Session = Depends(deps.get_db), *,
        file: UploadFile = File(...), request: Request
):
    db_obj = crud.attachment.create_by_file(db, file=file, request=request)
    result = {
        'uid': db_obj.uid,
        'url': db_obj.url
    }
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_201_CREATED)
