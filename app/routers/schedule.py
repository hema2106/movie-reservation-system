from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.schedule import ScheduleCreate, ScheduleResponse
from app.services.schedule import create_schedule
from app.database import SessionLocal
from app.models.schedule import Schedule
router = APIRouter()

def get_db() :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@router.post("/", response_model=ScheduleResponse)
def add_schedule(schedule: ScheduleCreate, db: Session = Depends(get_db)):
    return create_schedule(db=db, schedule=schedule)
@router.get("/", response_model=list[ScheduleResponse])
def get_schedules(db: Session = Depends(get_db)):
    return db.query(Schedule).all()