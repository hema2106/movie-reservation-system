from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.deps import get_db, require_admin
from app.models.theater import Theater
from app.schemas.theater import TheaterCreate, TheaterResponse
from app.services.theater import create_theater

router = APIRouter()


@router.post("/", response_model=TheaterResponse, dependencies=[Depends(require_admin)])
def add_theater(theater: TheaterCreate, db: Session = Depends(get_db)):
    return create_theater(db=db, theater=theater)

@router.get("/", response_model=list[TheaterResponse])
def get_theaters(db: Session = Depends(get_db)):
    return db.query(Theater).all()