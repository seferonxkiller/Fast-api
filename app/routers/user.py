from app import models, schemas, utils
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(
    prefix="/users",
    tags=['User']
)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("")
async def get_user(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return {"data": users}


@router.get("/{id}", response_model=schemas.UserOut)
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This user does not exists on database")
    return user
