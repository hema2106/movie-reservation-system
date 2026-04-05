from sqlalchemy import Column, Integer, String
from app.database import Base
class Theater(Base):
    __tablename__ = "theater"
    theater_id = Column(Integer, primary_key=True)
    theater_name = Column(String(100), nullable=False)
    theater_location = Column(String(200), nullable=False)
    total_capacity = Column(Integer,nullable=False)


