from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    # 自动生成数据库表名称
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

