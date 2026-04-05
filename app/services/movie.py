from sqlalchemy.orm import Session
from app.models.movie import Movie
from app.schemas.movie import MovieCreate

def  create_movie(db:Session,movie:MovieCreate):
    new_movie = Movie(
        movie_name=movie.movie_name,
        movie_type=movie.movie_type,
        duration=movie.duration,
        movie_language=movie.movie_language,
        cast_summary=movie.cast_summary
    )
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie
