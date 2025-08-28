from fastapi import FastAPI, Depends, HTTPException, APIRouter
from pydantic import BaseModel
import time
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal, get_db
from typing import Optional
from utils import hash_password
import oauth2

router = APIRouter(
    prefix = "/user",
    tags = ['User']
)

# create user
@router.post("/", response_model=schemas.UserOut, status_code=201)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(email = user.email, password = hash_password(user.password))

    if db.query(models.User).filter(models.User.email == new_user.email).first():
        raise HTTPException(status_code=409, detail=f"User with email {user.email} already exists")
        
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# get user information
@router.get("/{user_id}", response_model=schemas.UserOut)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    query = db.query(models.User).filter(models.User.id == user_id)

    user = query.first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

# delete user
@router.delete("/")
async def delete_user(db: Session = Depends(get_db), user: models.User = Depends(oauth2.get_current_user)):
    query = db.query(models.User).filter(models.User.id == user.id)
    query.delete(synchronize_session=False)
    db.commit()