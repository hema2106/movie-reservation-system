from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.theater import TheaterCreate, TheaterResponse
from app.services.theater import create_theater
from app.database import SessionLocal
from app.models.theater import Theater
router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TheaterResponse)
def add_theater(theater: TheaterCreate, db: Session = Depends(get_db)):
    return create_theater(db=db, theater=theater)

@router.get("/", response_model=list[TheaterResponse])
def get_theaters(db: Session = Depends(get_db)):
    return db.query(Theater).all()