# Import all models so SQLAlchemy registers them on Base.metadata (used by Alembic).
from app.models.user import Users
from app.models.theater import Theater
from app.models.movie import Movie
from app.models.seat import Seat
from app.models.schedule import Schedule
from app.models.ticket import Ticket

__all__ = ["Users", "Theater", "Movie", "Seat", "Schedule", "Ticket"]
