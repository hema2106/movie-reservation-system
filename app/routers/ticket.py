from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.deps import get_current_user, get_db
from app.models.ticket import Ticket
from app.models.user import Users
from app.schemas.ticket import TicketCreate, TicketResponse
from app.services.ticket import create_ticket

router = APIRouter()


@router.post("/", response_model=TicketResponse)
def book_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user),
):
    return create_ticket(db=db, ticket=ticket, user_id=current_user.id)


@router.get("/me", response_model=list[TicketResponse])
def get_my_tickets(
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user),
):
    return db.query(Ticket).filter(Ticket.user_id == current_user.id).all()
