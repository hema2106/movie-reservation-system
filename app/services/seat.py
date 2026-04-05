from sqlalchemy.orm import Session
from app.models.seat import Seat
from app.schemas.seat import SeatCreate
def create_seat(db: Session,seat: SeatCreate):
    new_seat = Seat(
        seat_row = seat.seat_row,
        seat_col = seat.seat_col,
        seat_type = seat.seat_type,
        theater_id = seat.theater_id,
    )
    db.add(new_seat)
    db.commit()
    db.refresh(new_seat)
    return new_seat