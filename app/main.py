from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user
from app.routers import theater
from app.routers import movie
from app.routers import seat
from app.routers import schedule
from app.routers import ticket
app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(theater.router, prefix="/theaters", tags=["Theaters"])
app.include_router(movie.router, prefix="/movies", tags=["Movies"])
app.include_router(seat.router, prefix="/seats", tags=["Seats"])
app.include_router(schedule.router, prefix="/schedules", tags=["Schedules"])
app.include_router(ticket.router, prefix="/tickets", tags=["Tickets"])
@app.get("/")
def greet():
    return {"message": "Welcome to Movie Reservation System"}