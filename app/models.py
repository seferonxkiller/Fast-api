from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, nullable=False, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
