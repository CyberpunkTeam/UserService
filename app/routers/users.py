from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.user_controller import UserController
from app.models.requests.user_update import UserUpdate
from app.models.users import Users
from app.repositories.users_repository import UsersRepository

router = APIRouter()

# Repository
user_repository = UsersRepository(config.DATABASE_URL, config.DATABASE_NAME)


@router.post("/users/", tags=["users"], response_model=Users, status_code=201)
async def create_user(user: Users):
    return UserController.post(user_repository, user)


@router.get("/users/", tags=["users"], response_model=List[Users])
async def list_users(uids: str = "", search: str = ""):
    if len(search) > 0:
        return UserController.search(user_repository, search)

    if len(uids) > 0:
        uids = uids[1 : len(uids) - 1].split(",")
        return UserController.get_users(user_repository, uids)

    return UserController.get(user_repository)


@router.get("/users/{uid}", tags=["users"], response_model=Users)
async def read_user(uid: str):
    return UserController.get(user_repository, uid, top=True)


@router.put("/users/{uid}", tags=["users"], response_model=Users)
async def update_user(uid: str, user: UserUpdate):
    return UserController.put(user_repository, uid, user)
