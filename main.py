from fastapi import FastAPI, HTTPException, Depends, Path, Query, Body
from typing import List, Dict, Optional, List, Annotated
from sqlalchemy.orm import Session

from fastapi.middleware.cors import CORSMiddleware

from models import Base, User, Post
from database import engine, session_local
from schemas import UserCreate, User as DbUser, PostCreate, PostResponse

app = FastAPI()

origins = [
    "http://localhost:5000",
    "http://127.0.0.1:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

# Пример GET-запроса
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/users/", response_model=DbUser)
async def create_user(user:  UserCreate, db: Session = Depends(get_db)) -> DbUser:
    db_user = User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

@app.post("/posts/", response_model=PostResponse)
async def create_post(post: PostCreate, db: Session = Depends(get_db)) -> PostResponse:
    db_user = db.query(User).filter(User.id == post.author_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    db_post = Post(title=post.title, body=post.body, author_id=post.author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post

@app.get("/posts/", response_model=List[PostResponse])
async def posts(db: Session = Depends(get_db)):
    return db.query(Post).all()
