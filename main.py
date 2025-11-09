from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class UserData(BaseModel):
    id: int
    fullname: str
    username: str
    password: str
@app.get("/hello")
def say_hello():
    return {"message": "Hello, Roba !"}

@app.post("/user/")
def create_user_simple(user: UserData):

    return user.dict()

@app.get("/user/{user_id}")
def read_user_simple(user_id: int):

    return {
        "message": "User data retrieved (GET)",
        "user_id": user_id,
        "fullname": "ru kha",
        "username": "user_123"
    }


@app.put("/user/{user_id}")
def update_user_simple(user_id: int, new_fullname: str):

    return {
        "id": user_id,
        "fullname": new_fullname,
        "message": "Fullname updated successfully"
    }


@app.delete("/user/{user_id}")
def delete_user_simple(user_id: int):
    return {
        "deleted_id": user_id,
        "message": "User deleted"
    }