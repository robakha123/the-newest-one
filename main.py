from typing import Union
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
DB_USERS: dict[str, UserData] = {}
app = FastAPI()
from request import UserData
@app.get("/hello")
def say_hello():
    return {"message": "Hello, Roba !"}


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
@app.post("/login", status_code=status.HTTP_200_OK)
def login_user(login_data: UserData):
    if login_data.username not in DB_USERS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    stored_user = DB_USERS[login_data.username]
    if stored_user.password != login_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    return {
        "message": "Login Successful",
        "user_id": stored_user.id,
        "fullname": stored_user.fullname
    }




@app.post("/user/", status_code=status.HTTP_201_CREATED)
def create_user_simple(user: UserData):
    if user.username in DB_USERS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    DB_USERS[user.username] = user
    return {
        "message": "User registered successfully",
        "user_data": user.dict()
    }
