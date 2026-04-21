from datetime import date, datetime, time

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.deps import get_db, require_admin
from app.models.schedule import Schedule
from app.schemas.schedule import ScheduleCreate, ScheduleResponse
from app.services.schedule import create_schedule

router = APIRouter()


@router.post("/", response_model=ScheduleResponse, dependencies=[Depends(require_admin)])
def add_schedule(schedule: ScheduleCreate, db: Session = Depends(get_db)):
    return create_schedule(db=db, schedule=schedule)


@router.get("/", response_model=list[ScheduleResponse])
def get_schedules(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Number of rows to skip"),
    limit: int = Query(100, ge=1, le=500, description="Max rows to return"),
    theater_id: int | None = Query(
        None,
        description="Filter by theater id",
    ),
    schedule_date: date | None = Query(
        None,
        description="Filter shows on this calendar date (local server date comparison on show_datetime)",
    ),
):
    q = db.query(Schedule)
    if theater_id is not None:
        q = q.filter(Schedule.theater_id == theater_id)
    if schedule_date is not None:
        start = datetime.combine(schedule_date, time.min)
        end = datetime.combine(schedule_date, time.max)
        q = q.filter(Schedule.show_datetime >= start, Schedule.show_datetime <= end)
    return q.order_by(Schedule.show_datetime).offset(skip).limit(limit).all()
