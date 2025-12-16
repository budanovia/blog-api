from fastapi import FastAPI, Depends, HTTPException, APIRouter
from pydantic import BaseModel
import time
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal, get_db
from typing import Optional, List
import oauth2
#import tag
import utils
import ast

import redis
from fastapi.encoders import jsonable_encoder
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

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
#@router.get("/{article_id}", response_model=schemas.ArticleOut)
@router.get("/{article_id}")
async def get_article(article_id: int, db: Session = Depends(get_db)):
    cache_key = f"article_id:{article_id}"
    
    # Check if the data exists in cache
    cached_data = redis_client.get(cache_key)
    if cached_data:
        print("got this from redis!")
        #return {"response": cached_data}
        #return cached_data
        cached_data_dict = json.loads(cached_data)
        return cached_data_dict
    
    # Fetch data from PostgreSQL DB
    '''response = requests.get(f"{WEATHER_API_URL}?key={API_KEY}&q={city}")
    weather_data = response.json()'''
    query = db.query(models.Article).filter(models.Article.id == article_id)
    article = query.first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    print("got this from db!")
    
    # Store the data in Redis cache with a 10-minute expiration
    article_data = jsonable_encoder(article)
    article_data_str = json.dumps(article_data)
    print(article_data_str)
    redis_client.setex(cache_key, 600, article_data_str)
    #redis_client.setex(cache_key, 600, article_data)
    
    return article
    '''cached_item = redis_client.get(f"article_{article_id}")
    
    if cached_item:
        #return {"article_id": article_id, "cached": True, "data": cached_item.decode('utf-8')}
        return cached_item.decode('utf-8')
    
    item_data = f"Item data for {article_id}"
    
    redis_client.set(f"article_{article_id}", item_data)'''


    '''query = db.query(models.Article).filter(models.Article.id == article_id)
    article = query.first()

    if not article:
        raise HTTPException(status_code=404, detail="Article not found")

    return article'''

# create article
@router.post("/", response_model=schemas.ArticleOut)
async def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db), user: models.User = Depends(oauth2.get_current_user)):
    # first converting the inputted tags string list from ArticleCreate schema into list of tag objects, that we can
    # then pass into models.Article so the article_tag association table is created
    
    #tags = article.tags
    tags = utils.generate_tags(article.content)
    tags = ast.literal_eval(tags)
    tags = [n.strip() for n in tags]
    print(tags)
    tag_objects_list = []
    for tag in tags:
        tagobj = db.query(models.Tag).filter(models.Tag.name == tag).first()
        if tagobj:
            tag_objects_list.append(tagobj)
            print("found " + tagobj.name)
        else:
            tagobj = models.Tag(name=tag)
            db.add(tagobj)
            db.commit()
            db.refresh(tagobj)
            tag_objects_list.append(tagobj)
            print("added " + tagobj.name)

    for tag in tag_objects_list:
        print("tag_objects_list entry: " + tag.name)
    new_post = models.Article(title=article.title, content=article.content, tags=tag_objects_list, user_id=user.id)
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