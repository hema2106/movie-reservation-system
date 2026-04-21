from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.deps import get_db, require_admin
from app.models.seat import Seat
from app.schemas.seat import SeatCreate, SeatResponse
from app.services.seat import create_seat

router = APIRouter()


@router.post("/", response_model=SeatResponse, dependencies=[Depends(require_admin)])
def add_seat(seat: SeatCreate, db: Session = Depends(get_db)):
    return create_seat(db=db, seat=seat)

@router.get("/{theater_id}", response_model=list[SeatResponse])
def get_seats(theater_id: int, db: Session = Depends(get_db)):
    return db.query(Seat).filter(Seat.theater_id == theater_id).all()