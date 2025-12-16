from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from database import Base

article_tag = Table("article_tag", Base.metadata,
                       Column("tag_id", ForeignKey("tags.id"), primary_key=True),
                       Column("article_id", ForeignKey("articles.id"), primary_key=True))

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    #tag = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="articles")
    #tag_id = Column(Integer, ForeignKey("tags.id", ondelete="CASCADE"), nullable=False)
    #tag_name = Column(String, ForeignKey("tags.name", ondelete="CASCADE"))
    tags = relationship("Tag",
                           secondary=article_tag,
                           back_populates="articles")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    articles = relationship("Article", back_populates="user")

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    #article_id = Column(Integer, ForeignKey("articles.id", ondelete="CASCADE"))
    #article_id = Column(Integer, ForeignKey("articles.id", ondelete="CASCADE"))
    articles = relationship("Article",
                           secondary=article_tag,
                           back_populates="tags")