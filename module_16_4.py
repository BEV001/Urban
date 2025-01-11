from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    username: str = Field(min_length=5, max_length=20, description="Enter username between 5 and 20 characters", example="UrbanUser")
    age: int = Field(ge=18, le=120, description="Enter age between 18 and 120", example=24)

# Пустой список пользователей
users: List[User] = []

@app.get("/")
async def get_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}")
async def add_user(username: str, age: int) -> User:
    user_id = users[-1].id + 1 if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> User:
    for index, user in enumerate(users):
        if user.id == user_id:
            removed_user = users.pop(index)
            return removed_user
    raise HTTPException(status_code=404, detail="User was not found")
