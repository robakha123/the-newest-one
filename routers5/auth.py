
from fastapi import APIRouter, HTTPException, status
from request import UserData

router = APIRouter(prefix="/login", tags=["auth"])
DB_USERS: dict[str, UserData] = {}

@router.post("/", status_code=status.HTTP_200_OK)
def login_user(login_data: UserData):
    if login_data.username not in DB_USERS or DB_USERS[login_data.username].password != login_data.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    stored_user = DB_USERS[login_data.username]
    return {
        "message": "Login Successful",
        "user_id": stored_user.id,
        "fullname": stored_user.fullname
    }
