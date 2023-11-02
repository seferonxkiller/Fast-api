from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class Post(BaseModel):
    title: str
    content: str
    # id: int
    published: bool = True
    # rating: Optional[int] = None


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None

