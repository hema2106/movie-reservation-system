from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.ticket import TicketCreate, TicketResponse
from app.services.ticket import create_ticket
from app.database import SessionLocal
from app.models.ticket import Ticket
router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/", response_model=TicketResponse)
def book_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    return create_ticket(db=db, ticket=ticket)

@router.get("/user/{user_id}", response_model=list[TicketResponse])
def get_user_tickets(user_id: int, db: Session = Depends(get_db)):
    return db.query(Ticket).filter(Ticket.user_id == user_id).all()