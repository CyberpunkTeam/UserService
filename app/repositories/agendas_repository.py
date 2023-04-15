from cpunk_mongo.db import DataBase

from app.models.agendas import Agendas


class AgendasRepository(DataBase):
    COLLECTION_NAME = "agendas"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def insert(self, agenda: Agendas):
        return self.save(self.COLLECTION_NAME, agenda)

    def get(self, uid=None, following_uid=None):
        filters = {}
        if uid is not None:
            filters["uid"] = uid

        if following_uid is not None:
            filters["following_uid"] = following_uid

        return self.filter(self.COLLECTION_NAME, filters, output_model=Agendas)
