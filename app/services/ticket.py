from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.schedule import Schedule
from app.models.seat import Seat
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate


def create_ticket(db: Session, ticket: TicketCreate, user_id: int):
    schedule = db.query(Schedule).filter(Schedule.id == ticket.schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")

    seat = db.query(Seat).filter(Seat.seat_id == ticket.seat_id).first()
    if not seat:
        raise HTTPException(status_code=404, detail="Seat not found")

    if seat.theater_id != schedule.theater_id:
        raise HTTPException(
            status_code=400,
            detail="Seat does not belong to the theater for this schedule",
        )

    new_ticket = Ticket(
        user_id=user_id,
        schedule_id=ticket.schedule_id,
        seat_id=ticket.seat_id,
        payment_status=ticket.payment_status,
        booking_time=datetime.now(),
    )
    db.add(new_ticket)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Seat already booked for this schedule",
        )
    db.refresh(new_ticket)
    return new_ticket
