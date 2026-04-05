from pydantic import BaseModel
from datetime import datetime

class TicketCreate(BaseModel):
    user_id: int
    schedule_id: int
    seat_id: int
    payment_status: str
class TicketResponse(BaseModel):
    ticket_id: int
    user_id: int
    schedule_id: int
    seat_id: int
    booking_time: datetime
    payment_status: str
    class Config:
        from_attributes = True