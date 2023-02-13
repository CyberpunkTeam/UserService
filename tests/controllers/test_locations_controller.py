import mongomock


from app import config
from app.controllers.location_controller import LocationController
from app.models.locations import Locations
from app.repositories.locations_repository import LocationsRepository


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_get_cities_and_country_start_with_bue():
    location_a = Locations(city="Buenos Aires", country="Argentina")
    location_b = Locations(city="La paz", country="Bolivia")

    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = LocationsRepository(url, db_name)

    ok = repository.insert_many([location_a, location_b])
    assert ok

    result = LocationController.search(repository, "bue")

    assert len(result) == 1
