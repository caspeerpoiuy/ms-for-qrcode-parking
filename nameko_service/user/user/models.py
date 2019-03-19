import datetime

from sqlalchemy import (
    Column, DateTime, Integer, VARCHAR, BOOLEAN,
)
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash


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


class UserModel(DeclarativeBase):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(VARCHAR(length=128), nullable=False)
    password = Column(VARCHAR(length=128), nullable=False)
    email = Column(VARCHAR(length=128), nullable=True)
    mobile = Column(Integer, nullable=True)
    nick_name = Column(VARCHAR(length=128), default=username)
    signature = Column(VARCHAR(length=128), default="he left nothing")
    avatar_url = Column(VARCHAR(length=256), default=None)
    last_login = Column(DateTime, default=datetime.datetime.utcnow)
    is_admin = Column(BOOLEAN, default=False)

