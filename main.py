from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import time
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, SessionLocal, get_db
from typing import Optional

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Starting page"}
    

# get all articles
@app.get("/articles")
async def get_all_articles(db: Session = Depends(get_db), tag: Optional[str] = None):
    query = db.query(models.Article)

    if tag:
        query = query.filter(models.Article.tag == tag)

    articles = query.all()

    return {"data": articles}

# create article
@app.post("/articles")
async def create_article(article: schemas.Article, db: Session = Depends(get_db)):
    new_post = models.Article(title=article.title, content=article.content, tag=article.tag)
    db.add(new_post)
    db.commit()
    # ORM equivalent of SQL 'RETURNING *'
    db.refresh(new_post)

    return {"data": new_post}


# get one article
@app.get("/articles/{article_id}")
async def get_article(article_id: int, db: Session = Depends(get_db)):
    query = db.query(models.Article).filter(models.Article.id == article_id)
    article = query.first()

    if not article:
        raise HTTPException(status_code=404, detail="Article not found")

    return {"data": article}

# delete article
@app.delete("/articles/{article_id}")
async def delete_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.id == article_id)

    if article.first() == None:
        raise HTTPException(status_code=404, detail="Article not found")

    article.delete(synchronize_session=False)
    db.commit()

# update article
@app.put("/articles/{article_id}")
async def update_article(article_id: int, updated_article: schemas.ArticleUpdate, db: Session = Depends(get_db)):
    query = db.query(models.Article).filter(models.Article.id == article_id)

    article = query.first()

    if article == None:
        raise HTTPException(status_code=404, detail="Article not found")

    query.update(updated_article.dict(), synchronize_session=False)
    db.commit()

    return {'data': query.first()}
