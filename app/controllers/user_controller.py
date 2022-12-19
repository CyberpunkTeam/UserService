from fastapi import HTTPException

from app.models.requests.user_update import UserUpdate
from app.models.users import Users


class UserController:
    @staticmethod
    def post(repository, user: Users):
        ok = repository.insert(user)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")
        return user

    @staticmethod
    def get(repository, uid=None, top=False):
        result = repository.get(uid)
        if len(result) == 0 and uid is not None:
            raise HTTPException(status_code=404, detail="User not found")

        if top:
            return result[0]
        return result

    @staticmethod
    def get_users(repository, uids):
        return repository.get_by_list(uids)

    @staticmethod
    def put(repository, uid, user: UserUpdate):
        UserController.exists(repository, uid)
        user.uid = uid
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
