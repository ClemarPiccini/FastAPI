from fastapi import APIRouter
from controllers.controllers import create_user
from model.models import User

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/Stefani")
def read_root():
    return {"Te amoooo"}

@router.post("/users")
def create_user_route(user: User):
    return create_user(user)
