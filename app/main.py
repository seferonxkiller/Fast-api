from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Optional
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Project1")

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

#
# try:
#     conn = psycopg2.connect(host='localhost', database='fastapi', user='fastapi', password='fastapi',
#                             cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("database connection was successfully!")
# except Exception as error:
#     print("Connection to database was failed")
#     print("Error", error)
#
# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
#             {"title": "favorite foods", "content": "I am programmer", "id": 2}]
#
#
# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p
#
#
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
#
#
# @app.get("/my-posts")
# async def get_posts():
#     return {"data": my_posts}
#
#
# @app.post("/createposts", status_code=status.HTTP_201_CREATED)
# async def create_post(new_post: Post):
#     post_dict = new_post.dict()
#     post_dict['id'] = randrange(0, 10000)
#     my_posts.append(post_dict)
#     return {"data": post_dict}
#
#
# @app.get("/post/{id}")
# async def get_post_id(id: int, response: Response):
#     posts = find_post(id)
#     if not posts:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This id does not have!!!!!!")
#     return {"data": posts}
#
#
# @app.get("/posts/latesposts")
# async def latest_posts():
#     post = my_posts[::-1]
#     return {"data": post}
#
#
# @app.delete("/posts/{id}")
# async def delete_post(id: int):
#     index = find_index_post(id)
#     if index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='With this id does not have post')
#     my_posts.pop(index)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
#
#
# @app.put("/posts/{id}")
# async def update_post(id: int, post: Post):
#     index = find_index_post(id)
#     if index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='With this id does not have post')
#     post_dict = post.dict()
#     post_dict['id'] = id
#     my_posts[index] = post_dict
#
#     return {"data": post_dict}
