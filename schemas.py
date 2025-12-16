from pydantic import BaseModel, EmailStr
from typing import Optional, List
import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime.datetime
    articles: "List[ArticleForUserOut]" = []

    class Config:
        from_attributes = True

class UserForArticleOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime.datetime

    class Config:
        from_attributes = True

# No longer needed. Replaced with OAuth2PasswordRequestForm.
#class UserLogin(UserCreate):
#    pass

# Pydantic model. The SQL alchemy model is in models.py.
class ArticleBase(BaseModel):
    title: str
    content: str
    # user_id: int  --> not needed anymore because of get_current_user() Dependency

class ArticleCreate(ArticleBase):
    #tags: List[str]
    pass

class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    #tag: Optional[str] = None

class ArticleOut(ArticleBase):
    id: int
    created_at: datetime.datetime
    user: UserForArticleOut
    #tags: List[str]
    
    class Config:
        from_attributes = True

class ArticleForUserOut(ArticleBase):
    created_at: datetime.datetime
    
    class Config:
        from_attributes = True

class TagCreate(BaseModel):
    name: str

class TagOut(BaseModel):
    id: int
    name: str

#UserOut.update_forward_refs(ArticleOut=ArticleOut)
ArticleOut.update_forward_refs()