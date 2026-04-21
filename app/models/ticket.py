from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, UniqueConstraint

from app.database import Base
from app.models.enums import PaymentStatus


class Ticket(Base):
    __tablename__ = "ticket"
    __table_args__ = (
        UniqueConstraint("schedule_id", "seat_id", name="uq_ticket_schedule_seat"),
    )

    ticket_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    schedule_id = Column(Integer, ForeignKey("schedules.id"), nullable=False)
    seat_id = Column(Integer, ForeignKey("seat.seat_id"), nullable=False)
    booking_time = Column(DateTime, nullable=False)
    payment_status = Column(
        Enum(
            PaymentStatus,
            values_callable=lambda obj: [e.value for e in obj],
            native_enum=False,
            length=20,
        ),
        nullable=False,
    )
