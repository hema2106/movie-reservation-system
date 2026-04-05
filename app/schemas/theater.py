from pydantic import BaseModel

class TheaterCreate(BaseModel):
    theater_name: str
    theater_location: str
    total_capacity: int
class TheaterResponse(BaseModel):
    theater_id: int
    theater_name: str
    theater_location: str
    total_capacity: int
    class Config:
        from_attributes=True