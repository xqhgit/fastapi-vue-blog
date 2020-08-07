from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from backend.utils import utils

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
    for image in images:
        items.append({
            'image': utils.img_base64(image)
        })
    total = len(items)
    items = items[offset:offset + limit]
    result = {
        "total": total,
        "items": items
    }
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
