from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.location_controller import LocationController

from app.models.locations import Locations
from app.repositories.locations_repository import LocationsRepository

router = APIRouter()

# Repository
location_repository = LocationsRepository(config.DATABASE_URL, config.DATABASE_NAME)


@router.get("/locations/", tags=["locations"], response_model=List[str])
async def list_users(search: str = ""):

    return LocationController.search(location_repository, search)
