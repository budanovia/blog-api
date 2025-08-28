from fastapi import FastAPI, Depends, HTTPException, APIRouter
from pydantic import BaseModel
import time
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal, get_db
from typing import Optional, List
import oauth2

router = APIRouter(
    prefix = "/articles",
    tags = ['Articles']
)

# get all articles
@router.get("/")
async def get_all_articles(db: Session = Depends(get_db), tag: Optional[str] = None, user_id: Optional[int] = None, limit: Optional[int] = 20, skip: Optional[int] = 0):
    query = db.query(models.Article)

    if tag:
        query = query.filter(models.Article.tag == tag)

    if user_id:
        query = query.filter(models.Article.user_id == user_id)

    query = query.limit(limit)
    query = query.offset(skip)

    articles = query.all()

    return articles

# get one article
@router.get("/{article_id}", response_model=schemas.ArticleOut)
async def get_article(article_id: int, db: Session = Depends(get_db)):
    query = db.query(models.Article).filter(models.Article.id == article_id)
    article = query.first()

    if not article:
        raise HTTPException(status_code=404, detail="Article not found")

    return article

# create article
@router.post("/", response_model=schemas.ArticleOut)
async def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db), user: models.User = Depends(oauth2.get_current_user)):
    new_post = models.Article(title=article.title, content=article.content, tag=article.tag, user_id=user.id)
    db.add(new_post)
    db.commit()
    # ORM equivalent of SQL 'RETURNING *'
    db.refresh(new_post)

    return new_post

# delete article
@router.delete("/{article_id}")
async def delete_article(article_id: int, db: Session = Depends(get_db), user: models.User = Depends(oauth2.get_current_user)):
    query = db.query(models.Article).filter(models.Article.id == article_id)
    article = query.first()

    if article == None:
        raise HTTPException(status_code=404, detail="Article not found")

    if article.user_id != user.id:
        raise HTTPException(status_code=403, detail="Forbidden")

    query.delete(synchronize_session=False)
    db.commit()

# update article
@router.put("/{article_id}")
async def update_article(article_id: int, updated_article: schemas.ArticleUpdate, db: Session = Depends(get_db), user: models.User = Depends(oauth2.get_current_user)):
    query = db.query(models.Article).filter(models.Article.id == article_id)

    article = query.first()

    if article == None:
        raise HTTPException(status_code=404, detail="Article not found")

    if article.user_id != user.id:
        raise HTTPException(status_code=403, detail="Forbidden")

    query.update(updated_article.dict(), synchronize_session=False)
    db.commit()

    return query.first()