from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.category import Category

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/categories")
def create_category(name: str, db: Session = Depends(get_db)):
    category = Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


@router.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()