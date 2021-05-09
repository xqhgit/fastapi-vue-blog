from typing import Optional
from sqlalchemy.orm import Session

from app.models import Admin
from app.crud.base import CRUDBase
from app.schemas.admin import AdminCreate, AdminUpdate
from app.core.security import get_password_hash, verify_password


class CRUDAdmin(CRUDBase[Admin, AdminCreate, AdminUpdate]):

    def create(self, db: Session, *, obj_in: AdminCreate) -> Admin:
        db_obj = Admin(
            username=obj_in.username,
            password_hash=get_password_hash(obj_in.password),
            email=obj_in.email
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def authenticate(self, db: Session, *, username: str, password: str) -> Optional[Admin]:
        obj: Admin = db.query(Admin).filter(Admin.username == username).first()
        if not obj:
            return None
        if not verify_password(password, obj.password_hash):
            return None
        return obj


admin = CRUDAdmin(Admin)


