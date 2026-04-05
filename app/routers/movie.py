from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.movie import MovieCreate, MovieResponse
from app.services.movie import create_movie
from app.database import SessionLocal
from app.models.movie import Movie
router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.get("/", response_model=list[MovieResponse])
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()


@router.post("/", response_model=MovieResponse)
def add_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return create_movie(db=db, movie=movie)