# -*-coding:utf-8-*-
# fix toModuleNotFound
import logging
from app.db.session import engine, SessionLocal
from app.db.base import Base
from app.models import *
from app import crud, schemas

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def create_admin():
    db = SessionLocal()
    obj_in = schemas.AdminCreate(
        username='admin',
        password='admin',
        email='1104440778@qq.com'
    )
    obj = crud.admin.create(db, obj_in=obj_in)
    print(obj)
    return obj


def init() -> None:
    create_admin()


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
