from sqlalchemy.orm import Session
from backend import crud, schemas
from backend.core.config import settings


def init_db(db: Session) -> None:
    user = crud.user.get_by_username(db, username=settings.FIRST_ADMIN)
    if not user:
        user_in = schemas.UserCreate(
            username=settings.FIRST_ADMIN,
            password=settings.FIRST_ADMIN_PASSWORD,
            is_admin=True,
            email='test@qq.com'
        )
        crud.user.create(db, obj_in=user_in)


