from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate
from datetime import datetime


def create_ticket(db: Session, ticket: TicketCreate):
    existing_ticket = db.query(Ticket).filter(
        Ticket.seat_id == ticket.seat_id,
        Ticket.schedule_id == ticket.schedule_id
    ).first()
    if existing_ticket:
        raise HTTPException(status_code=400, detail="Seat already booked for this schedule")

    new_ticket = Ticket(
        user_id=ticket.user_id,
        schedule_id=ticket.schedule_id,
        seat_id=ticket.seat_id,
        payment_status=ticket.payment_status,
        booking_time=datetime.now()
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket
    raise HTTPException(status_code=400, detail="Seat already booked for this schedule")
