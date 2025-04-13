from pydantic import BaseModel
import sqlite3


class UserBase(BaseModel):
    name: str
    age: int


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    name: str
    age: int

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    title: str
    body: str
    author_id: int

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    title: str
    body: str
    author_id: int
    id: int
    author: User

    class Config:
        from_attributes = True
