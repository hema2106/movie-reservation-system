from pydantic import BaseModel
from datetime import datetime
class ScheduleCreate(BaseModel):
    movie_id: int
    theater_id: int
    show_datetime: datetime
    ticket_price: float
class ScheduleResponse(BaseModel):
    id: int
    movie_id: int
    theater_id: int
    show_datetime: datetime
    ticket_price: float
    class Config:
        from_attributes=True