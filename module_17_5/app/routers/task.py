from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session # Сессия БД
from app.backend.db_depends import get_db # Функция подключения к БД
from typing import Annotated # Аннотации, Модели БД и Pydantic.

from app.models.task import Task
from app.models.user import User
from app.schemas import CreateTask, UpdateTask # Функции работы с записями.

from sqlalchemy import insert, select, update, delete
from slugify import slugify # Функция создания slug-строки


router = APIRouter(
    prefix="/tasks",
    tags=["task"]
)

@router.get("/")
async def all_useall_tasksrs(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

@router.get("/{task_id}")
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task:
        return task
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")

@router.post("/create")
async def create_task(new_task: CreateTask, user_id: int,  db: Annotated[Session, Depends(get_db)]):
    # Проверяем, существует ли пользователь, которому будет назначена задача
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    else:
        db.execute(insert(Task).values(title=new_task.title,
                                       content=new_task.content,
                                       priority=new_task.priority,
                                       slug=slugify(new_task.title),
                                       user_id=user_id,
                                       ))
        db.commit()
        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'
        }


@router.put("/update")
async def update_task(task_id: int, update_task: UpdateTask,
                      db: Annotated[Session, Depends(get_db)]):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task:
        db.execute(update(Task).values(title=update_task.title,
                                       content=update_task.content,
                                       priority=update_task.priority
                                       ))
        db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'Task update is successful!'
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found"
        )



@router.delete("/delete")
async def delete_task(task_id: int,
                      db: Annotated[Session, Depends(get_db)]):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task:
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'Task was successfully deleted!'
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found"
        )
