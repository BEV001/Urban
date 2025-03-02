from fastapi import FastAPI
from routers import task, user

app = FastAPI()

# Подключение роутеров
app.include_router(task.router)
app.include_router(user.router)

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}
