from pydantic import BaseModel
class MovieCreate(BaseModel):
    movie_name: str
    movie_type: str
    duration: int
    movie_language: str
    cast_summary:str
class MovieResponse(BaseModel):
    id: int
    movie_name: str
    movie_type: str
    duration: int
    movie_language: str
    cast_summary:str
    class Config:
        from_attributes= True

