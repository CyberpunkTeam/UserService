from cpunk_mongo.db import DataBase

from app.models.users import Users


class UsersRepository(DataBase):
    COLLECTION_NAME = "users"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, email=None):
        if email is None:
            return self.filter(self.COLLECTION_NAME, {}, output_model=Users)
        return self.find_by(self.COLLECTION_NAME, "email", email, output_model=Users)

    def insert(self, user: Users):
        return self.save(self.COLLECTION_NAME, user)

    @staticmethod
    def create_repository(url, database_name):
        return UsersRepository(url, database_name)
