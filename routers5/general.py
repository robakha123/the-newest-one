from fastapi import APIRouter

router = APIRouter(tags=["general"])

@router.get("/hello")
def say_hello():
    return {"message": "Hello, Roba !"}
