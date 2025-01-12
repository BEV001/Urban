from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session # Сессия БД
from app.backend.db_depends import get_db # Функция подключения к БД
from typing import Annotated # Аннотации, Модели БД и Pydantic.
from app.models.user import User
from app.schemas import CreateUser, UpdateUser # Функции работы с записями.
from sqlalchemy import insert, select, update, delete
from slugify import slugify # Функция создания slug-строки

router = APIRouter(
    prefix="/users",
    tags=["user"]
)

@router.get("/all_users")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users

@router.get("/{user_id}")
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

@router.post("/create")
async def create_user(new_user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    # Проверка существует ли пользователь с такими данными
    existing_user = db.scalars(select(User).where(User.username == new_user.username)).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username combination already exists"
        )
    else:
        db.execute(insert(User).values(username=new_user.username,
                                       firstname=new_user.firstname,
                                       lastname=new_user.lastname,
                                       age=new_user.age,
                                       slug=slugify(new_user.username)))
        db.commit()
        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'
        }

@router.put("/update/{user_id}")
async def update_user(user_id: int, update_user: UpdateUser,
                      db: Annotated[Session, Depends(get_db)]):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user:
        db.execute(update(User).where(User.id == user_id).values(
            firstname=update_user.firstname,
            lastname=update_user.lastname,
            age=update_user.age))
        db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'User update is successful!'
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )



@router.delete("/delete/{user_id}")
async def delete_user(user_id: int,
                      db: Annotated[Session, Depends(get_db)]):
    user = db.scalars(select(User).where(User.id == user_id))
    if user:
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'User was successfully deleted!'
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )
