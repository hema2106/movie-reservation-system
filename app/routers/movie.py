from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.deps import get_db, require_admin
from app.models.movie import Movie
from app.schemas.movie import MovieCreate, MovieResponse
from app.services.movie import create_movie

router = APIRouter()


@router.get("/", response_model=list[MovieResponse])
def get_movies(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Number of rows to skip"),
    limit: int = Query(100, ge=1, le=500, description="Max rows to return"),
):
    return db.query(Movie).offset(skip).limit(limit).all()


@router.post("/", response_model=MovieResponse, dependencies=[Depends(require_admin)])
def add_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return create_movie(db=db, movie=movie)
