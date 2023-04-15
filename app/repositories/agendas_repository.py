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

    def get(self, aid=None, following_uid=None, agenda_type=None):
        filters = {}
        if aid is not None:
            filters["aid"] = aid

        if following_uid is not None:
            filters["following_uid"] = following_uid

        if agenda_type is not None:
            filters["agenda_type"] = agenda_type

        return self.filter(self.COLLECTION_NAME, filters, output_model=Agendas)

    def reset(self):
        return self.delete_all(self.COLLECTION_NAME)
