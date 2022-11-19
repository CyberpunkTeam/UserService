from typing import List

from fastapi import APIRouter

from app.controllers.user_controller import UserController
from app.models.user import User

router = APIRouter()


@router.get("/users/", tags=["users"], response_model=List[User])
async def read_users():
    return UserController.get()

