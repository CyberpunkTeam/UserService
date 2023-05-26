from fastapi import HTTPException
from datetime import datetime

from app.models.agendas import Agendas
from app.models.requests.user_update import UserUpdate
from app.models.states import States
from app.models.users import Users
from app.models.response.users import Users as UsersResponse


class UserController:
    @staticmethod
    def post(repository, user: Users, agenda_repository):
        user.set_default_images()
        local = datetime.now()
        user.created_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        user.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        user.state = States.ACTIVE
        user.temporal_team = False
        ok = repository.insert(user)

        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")

        return UserController.get(
            repository, user.uid, top=True, agenda_repository=agenda_repository
        )

    @staticmethod
    def get(repository, uid=None, top=False, agenda_repository=None):
        result = repository.get(uid)
        if len(result) == 0 and uid is not None:
            raise HTTPException(status_code=404, detail="User not found")

        if top:
            user = result[0]
            uid = user.uid
            users_following = agenda_repository.get(aid=uid, agenda_type="USERS")
            users_followers = agenda_repository.get(
                following_uid=uid, agenda_type="USERS"
            )
            teams_following = agenda_repository.get(aid=uid, agenda_type="TEAMS")

            user_json = user.to_json()
            user_json["following"] = {
                "users": [agenda.following_uid for agenda in users_following],
                "teams": [agenda.following_uid for agenda in teams_following],
            }
            user_json["followers"] = [agenda.aid for agenda in users_followers]
            user_response = UsersResponse(**user_json)

            return user_response
        return result

    @staticmethod
    def get_users(repository, uids):
        return repository.get_by_list(uids)

    @staticmethod
    def put(repository, uid, user: UserUpdate, agenda_repository):
        UserController.exists(repository, uid)
        user.uid = uid
        local = datetime.now()
        user.updated_date = local.strftime("%d-%m-%Y:%H:%M:%S")
        if repository.put(user):
            return UserController.get(
                repository, user.uid, top=True, agenda_repository=agenda_repository
            )
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
    def add_follower(agenda_repository, uid, follower_uid, follower_type):
        new_agenda = Agendas(
            aid=follower_uid, following_uid=uid, agenda_type=follower_type
        )
        ok = agenda_repository.insert(new_agenda)
        if not ok:
            raise HTTPException(status_code=404, detail="Error to save agenda")
