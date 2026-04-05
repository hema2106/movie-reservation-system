from pydantic import BaseModel
class SeatCreate(BaseModel):
    seat_row: str
    seat_col: int
    seat_type: str
    theater_id: int
class SeatResponse(BaseModel):
    seat_id: int
    seat_row: str
    seat_col: int
    seat_type: str
    theater_id: int
    class Config:
        from_attributes= True
