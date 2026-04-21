from datetime import datetime

from pydantic import BaseModel

from app.models.enums import PaymentStatus


class TicketCreate(BaseModel):
    schedule_id: int
    seat_id: int
    payment_status: PaymentStatus


class TicketResponse(BaseModel):
    ticket_id: int
    user_id: int
    schedule_id: int
    seat_id: int
    booking_time: datetime
    payment_status: PaymentStatus

    class Config:
        from_attributes = True
