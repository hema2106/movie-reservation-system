from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
class Ticket(Base):
    __tablename__ = "ticket"
    ticket_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    schedule_id = Column(Integer, ForeignKey("schedules.id"), nullable=False)
    seat_id = Column(Integer, ForeignKey("seat.seat_id"), nullable=False)
    booking_time = Column(DateTime, nullable=False)
    payment_status=Column(String(50), nullable=False)
