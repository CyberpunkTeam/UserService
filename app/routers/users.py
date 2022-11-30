from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.user_controller import UserController
from app.models.users import Users
from app.repositories.users_repository import UsersRepository

router = APIRouter()

# Repository
user_repository = UsersRepository(config.DATABASE_URL, config.DATABASE_NAME)


@router.post("/users/", tags=["users"], response_model=Users, status_code=201)
async def create_user(user: Users):
    return UserController.post(user_repository, user)


@router.get("/users/", tags=["users"], response_model=List[Users])
async def list_users():
    return UserController.get(user_repository)


@router.get("/users/{user_id}", tags=["users"], response_model=Users)
async def read_user(user_id: str):
    return UserController.get(user_repository, user_id)
