from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from app.database import Base
class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movie.id'), nullable=False)
    theater_id = Column(Integer, ForeignKey('theater.theater_id'), nullable=False)
    show_datetime=Column(DateTime, nullable=False)
    ticket_price=Column(Float,nullable=False)

