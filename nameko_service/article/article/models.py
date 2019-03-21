import datetime
from sqlalchemy import (
    Column, DateTime, Integer, VARCHAR,ForeignKey,
    )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Base(object):
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )


DeclarativeBase = declarative_base(cls=Base)


class ArticleModel(DeclarativeBase):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    headline = Column(VARCHAR(length=128), nullable=False)
    digest = Column(VARCHAR(length=512), nullable=False)
    content = Column(VARCHAR(length=10240), nullable=False)
    reading_quantity = Column(Integer, default=0)
    index_image_url = Column(VARCHAR(length=256))

    author_id = Column(
        Integer,
        ForeignKey("author.id", name="fk_author_id"),
        nullable=False,
        index=True
    )
    category_id = Column(
        Integer,
        ForeignKey("category.id", name="fk_category_id"),
        nullable=False,
        index=True
    )
    comments = relationship("CommentModel", lazy="dynamic")


class CategoryModel(DeclarativeBase):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    category_name = Column(VARCHAR(length=128), nullable=False)
    article_list = relationship("ArticleModel", backref="category", lazy="dynamic")


class CommentModel(DeclarativeBase):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(
        Integer,
        ForeignKey("user.id", name="fk_user_id"),
        nullable=False,
        index=True
    )
    article_id = Column(
        Integer,
        ForeignKey("user.id", name="fk_user_id"),
        nullable=False,
        index=True
    )


class PraiseModel(DeclarativeBase):
    __tablename__ = "praise"

    comment_id = Column