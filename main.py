from fastapi import FastAPI, Depends, HTTPException
#from pydantic import BaseModel
#import time
#from sqlalchemy.orm import Session
import models
#import schemas
from database import engine, SessionLocal, get_db
#from typing import Optional
from routers import article, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(article.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Starting page"}