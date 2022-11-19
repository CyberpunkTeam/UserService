from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["users"])
async def ping():
    return "pong"
