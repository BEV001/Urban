from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/")
async def root() -> str:
    return "Главная страница"


@app.get("/users")
async def get_users() -> dict[str, str]:
    return users


@app.post("/user/{username}/{age}")
async def add_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]
) -> str:
    user_id = str(max(int(key) for key in users.keys()) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(ge=0, description="Enter user id to update", example=1)],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]
) -> str:
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=0, description="Enter user id to delete", example=1)],
) -> str:
    user_id_str = str(user_id)
    if user_id_str not in users:
        return f"User {user_id} does not exist"
    del users[user_id_str]
    return f'The user {user_id} is deleted'
