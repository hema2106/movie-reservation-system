from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.deps import get_db
from app.schemas.user import UserCreate, UserLogin, UserResponse, TokenResponse
from app.services.user import create_user, login_user

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    result = login_user(db=db, email=user.email, password=user.password)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return result

