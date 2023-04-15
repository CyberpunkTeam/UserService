from fastapi import HTTPException
from datetime import datetime

from app.models.agendas import Agendas
from app.models.requests.user_update import UserUpdate
from app.models.users import Users
from app.models.response.users import Users as UsersResponse


class UserController:
    @staticmethod
    def post(repository, user: Users):
        user.set_default_images()
        local = datetime.now()
        user.created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        user.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        ok = repository.insert(user)

        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")
        return user

    @staticmethod
    def get(repository, uid=None, top=False, agenda_repository=None):
        result = repository.get(uid)
        if len(result) == 0 and uid is not None:
            raise HTTPException(status_code=404, detail="User not found")

        if top:
            user = result[0]
            uid = user.uid
            following = agenda_repository.get(uid=uid)
            followers = agenda_repository.get(following_uid=uid)
            user_json = user.to_json()
            user_json["following"] = [agenda.following_uid for agenda in following]
            user_json["followers"] = [agenda.following_uid for agenda in followers]
            user_response = UsersResponse(**user_json)

            return user_response
        return result

    @staticmethod
    def get_users(repository, uids):
        return repository.get_by_list(uids)

    @staticmethod
    def put(repository, uid, user: UserUpdate):
        UserController.exists(repository, uid)
        user.uid = uid
        local = datetime.now()
        user.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        if repository.put(user):
            result = repository.get(uid=uid)
            return result[0]
        else:
            raise HTTPException(status_code=500, detail="Error to update user")

    @staticmethod
    def exists(repository, uid):
        result = repository.get(uid)
        if len(result) == 0 and uid is not None:
            raise HTTPException(status_code=404, detail="User not found")

    @staticmethod
    def search(repository, value):
        fields = ["name", "lastname"]
        return repository.search(fields, value)

    @staticmethod
    def add_follower(agenda_repository, uid, follower_uid):
        new_agenda = Agendas(uid=follower_uid, following_uid=uid)
        ok = agenda_repository.insert(new_agenda)
        if not ok:
            raise HTTPException(status_code=404, detail="Error to save agenda")
