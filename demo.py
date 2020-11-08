from sqlalchemy.orm import Session
from backend import crud, models
from backend.db.session import SessionLocal

db: Session = SessionLocal()
result = crud.category.get_list(db)
print(result)
