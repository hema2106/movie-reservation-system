from sqlalchemy.orm import Session
from app.models.schedule import Schedule
from app.schemas.schedule import ScheduleCreate

def create_schedule(db: Session, schedule: ScheduleCreate):
    new_schedule=Schedule(
        movie_id=schedule.movie_id,
        theater_id=schedule.theater_id,
        show_datetime=schedule.show_datetime,
        ticket_price=schedule.ticket_price,
    )
    db.add(new_schedule)
    db.commit()
    db.refresh(new_schedule)
    return new_schedule