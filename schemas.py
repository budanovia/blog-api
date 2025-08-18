from pydantic import BaseModel
from typing import Optional

# Pydantic model. The SQL alchemy model is in models.py.
class Article(BaseModel):
    title: str
    content: str
    tag: str

class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    tag: Optional[str] = None