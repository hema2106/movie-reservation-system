from sqlalchemy import Column, Integer, String
from app.database import Base
class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    movie_name = Column(String(100), nullable=False)
    movie_type = Column(String(100), nullable=False)
    duration = Column(Integer, nullable=False)
    movie_language = Column(String(100), nullable=False)
    cast_summary = Column(String(500), nullable=False)
