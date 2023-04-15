from cpunk_mongo.db import DataBase

from app.models.requests.user_update import UserUpdate
from app.models.users import Users


class UsersRepository(DataBase):
    COLLECTION_NAME = "users"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, uid=None):
        if uid is None:
            return self.filter(self.COLLECTION_NAME, {}, output_model=Users)
        return self.find_by(self.COLLECTION_NAME, "uid", uid, output_model=Users)

    def get_by_list(self, uid_list):
        result = self.find_by(
            self.COLLECTION_NAME, "uid", {"$in": uid_list}, output_model=Users
        )
        if len(result) > 0:
            result.sort(key=lambda thing: uid_list.index(thing.uid))

        return result

    def insert(self, user: Users):
        return self.save(self.COLLECTION_NAME, user)

    def put(self, user: UserUpdate):
        return self.update(self.COLLECTION_NAME, "uid", user.uid, user)

    def search(self, fields, value):
        return self.ilike(self.COLLECTION_NAME, fields, value, output_model=Users)

    def reset(self):
        return self.delete_all(self.COLLECTION_NAME)

    @staticmethod
    def create_repository(url, database_name):
        return UsersRepository(url, database_name)
