from fastapi import FastAPI, Depends, HTTPException, APIRouter
from pydantic import BaseModel
import time
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal, get_db
from typing import Optional, List
import oauth2

router = APIRouter(
    prefix = "/tags",
    tags = ['Tags']
)

# create tag
@router.post("/", response_model=schemas.TagOut)
async def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    new_tag = models.Tag(name=tag.name)
    db.add(new_tag)
    db.commit()
    # ORM equivalent of SQL 'RETURNING *'
    db.refresh(new_tag)

    return new_tag