from sqlalchemy.orm import Session
from app.models.theater import Theater
from app.schemas.theater import TheaterCreate
def create_theater(db: Session,theater:TheaterCreate):
    new_theater = Theater(
        theater_name=theater.theater_name,
        theater_location=theater.theater_location,
        total_capacity=theater.total_capacity
    )
    db.add(new_theater)
    db.commit()
    db.refresh(new_theater)
    return new_theater
