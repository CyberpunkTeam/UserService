from typing import List

from cpunk_mongo.db import DataBase

from app.models.locations import Locations


class LocationsRepository(DataBase):
    COLLECTION_NAME = "locations"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def insert(self, location: Locations):
        return self.save(self.COLLECTION_NAME, location)

    def insert_many(self, locations: List[Locations]):
        return self.save_many(self.COLLECTION_NAME, locations)

    def search(self, fields, value):
        return self.ilike(self.COLLECTION_NAME, fields, value, output_model=Locations)
