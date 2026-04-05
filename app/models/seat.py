from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base
class Seat(Base):
    __tablename__ = 'seat'
    seat_id= Column(Integer, primary_key=True)

    seat_row = Column(String(10), nullable=False)
    seat_col= Column(Integer,nullable=False)
    seat_type= Column(String(50),nullable=False)
    theater_id=Column(Integer,ForeignKey("theater.theater_id"),nullable=False)
