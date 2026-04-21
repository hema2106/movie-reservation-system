import os

from dotenv import load_dotenv
from fastapi import Depends, FastAPI

load_dotenv()
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.deps import get_db
from app.routers import movie, schedule, seat, theater, ticket, user


def _cors_origins():
    raw = os.getenv("ALLOWED_ORIGINS", "*").strip()
    if raw == "*":
        return ["*"], False
    origins = [o.strip() for o in raw.split(",") if o.strip()]
    if not origins:
        return ["*"], False
    return origins, True


_origins, _creds = _cors_origins()

app = FastAPI(title="Movie Reservation System", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins,
    allow_credentials=_creds,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(theater.router, prefix="/theaters", tags=["Theaters"])
app.include_router(movie.router, prefix="/movies", tags=["Movies"])
app.include_router(seat.router, prefix="/seats", tags=["Seats"])
app.include_router(schedule.router, prefix="/schedules", tags=["Schedules"])
app.include_router(ticket.router, prefix="/tickets", tags=["Tickets"])


@app.get("/")
def greet():
    return {"message": "Welcome to Movie Reservation System"}


@app.get("/health")
def health(db: Session = Depends(get_db)):
    """Liveness + database connectivity (for load balancers / orchestration)."""
    db.execute(text("SELECT 1"))
    return {"status": "ok"}
