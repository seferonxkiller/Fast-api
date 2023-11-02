from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas, oauth2

router = APIRouter()


@router.get("/sql-post")
async def test_posts(db: Session = Depends(get_db)):
    a = db.query(models.Post).all()
    return {"status": a}


@router.post("/sql-post", status_code=status.HTTP_201_CREATED)
async def create_post(post: schemas.Post, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    # new_post = models.Post(title=post.title, content=post.content, published=post.published)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}


@router.get("/posts/{id}")
async def get_id(id: int, db: Session = Depends(get_db)):
    posts = db.query(models.Post).filter(models.Post.id == id).first()

    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This id does not have!!!!!!")
    return {"data": posts}


@router.delete("/posts/{id}", status_code=status.HTTP_404_NOT_FOUND)
async def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exists")

    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.put("/posts/{id}")
async def update_post(id: int, updated_post: schemas.Post, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"with this id {id} does not exists")
    post_query.update(updated_post.dict(), synchronize_session=False)

    db.commit()

    return {"data": post_query.first()}


@router.get("/latest-posts")
async def latest_posts(db: Session = Depends(get_db)):
    post_query = db.query(models.Post).all()[:-4:-1]
    print(post_query)
    if post_query == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"I don't know")

    return {"data": post_query}

#role based authontification
