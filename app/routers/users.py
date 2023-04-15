import os
from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.user_controller import UserController
from app.models.requests.user_update import UserUpdate
from app.models.users import Users
from app.repositories.agendas_repository import AgendasRepository
from app.repositories.users_repository import UsersRepository
from app.models.response.users import Users as UserResponse

router = APIRouter()

# Repository
user_repository = UsersRepository(config.DATABASE_URL, config.DATABASE_NAME)
agenda_repository = AgendasRepository(config.DATABASE_URL, config.DATABASE_NAME)


@router.post("/users/reset", tags=["teams"], status_code=200)
async def reset():
    if os.environ.get("TEST_MODE") == "1":
        return {
            "reset_users": user_repository.reset(),
            "reset_agendas": agenda_repository.reset(),
        }


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


@router.get("/users/{uid}", tags=["users"], response_model=UserResponse)
async def read_user(uid: str):
    return UserController.get(
        user_repository, uid, top=True, agenda_repository=agenda_repository
    )


@router.post(
    "/users/{uid}/followers/{follower_uid}",
    tags=["users"],
    status_code=201,
    response_model=UserResponse,
)
async def add_follower(uid: str, follower_uid: str):
    UserController.add_follower(agenda_repository, uid, follower_uid)
    return UserController.get(
        user_repository, follower_uid, top=True, agenda_repository=agenda_repository
    )


@router.put("/users/{uid}", tags=["users"], response_model=Users)
async def update_user(uid: str, user: UserUpdate):
    return UserController.put(user_repository, uid, user)
