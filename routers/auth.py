from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
import time
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal, get_db
from typing import Optional
from utils import verify_password
from oauth2 import create_access_token

router = APIRouter(
    prefix = "/login",
    tags = ['Auth']
)


@router.post("/")
async def login_user(user_login: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    query = db.query(models.User).filter(models.User.email == user_login.username)
    user = query.first()
    if user == None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    verification = verify_password(user_login.password, user.password)
    if not verification:
        raise HTTPException(status_code=401, detail=f"Invalid credentials")

    token = create_access_token({"user_id": user.id})

    return {"access_token": token, "token_type": "bearer"}