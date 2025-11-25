
from fastapi import FastAPI
from routers5.users import router as users_router
from routers5.auth import router as auth_router
from routers5.general import router as general_router

app = FastAPI()

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(general_router)
