
from fastapi import APIRouter, HTTPException, status
from request import UserData

router = APIRouter(prefix="/user", tags=["users"])
DB_USERS: dict[str, UserData] = {}

@router.get("/{user_id}")
def read_user_simple(user_id: int):
    return {
        "message": "User data retrieved (GET)",
        "user_id": user_id,
        "fullname": "ru kha",
        "username": "user_123"
    }

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user_simple(user: UserData):
    if user.username in DB_USERS:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    DB_USERS[user.username] = user
    return {"message": "User registered successfully", "user_data": user.dict()}

@router.put("/{user_id}")
def update_user_simple(user_id: int, new_fullname: str):
    return {"id": user_id, "fullname": new_fullname, "message": "Fullname updated successfully"}

@router.delete("/{user_id}")
def delete_user_simple(user_id: int):
    return {"deleted_id": user_id, "message": "User deleted"}
