from fastapi import FastAPI, HTTPException
from typing import Dict, Optional, List
from pydantic import BaseModel

app = FastAPI()  # создаем обект этого класса не передаем параметры


class Post(BaseModel):
    id: int
    title: str
    body: str


posts = [
    {'id': 1, 'title': 'News 1', 'body': 'Text 1'},
    {'id': 2, 'title': 'News 2', 'body': 'Text 2'},
    {'id': 3, 'title': 'News 3', 'body': 'Text 3'},
]

# @app.get("/items")
# async def items() -> list[Post]:
#    post_objects = []
#    for post in posts:
#        post_objects.append(Post(id=post['id'], title=post['title'], body=post['body']))
#     return posts

@app.get("/items")
async def items() -> list[Post]:
    return [Post(**post) for post in posts]

@app.get("/items/{id}")
async def items(id: int) -> Post:
    for post in posts:
        if post['id'] == id:
            return Post(**post)

    raise HTTPException(status_code=404, detail='POST not found')

@app.get("/search")
async def search(post_id: Optional[int] = None) -> Dict[str, Optional[Post]]:
    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return {"data": Post(**post)}
        raise HTTPException(status_code=404, detail='POST not found')
    else:
        return {"data": None}
