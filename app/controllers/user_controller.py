from fastapi import HTTPException
from app.models.users import Users


class UserController:
    @staticmethod
    def post(repository, user: Users):
        ok = repository.insert(user)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")
        return user

    @staticmethod
    def get(repository, email=None, top=False):
        result = repository.get(email)
        if len(result) == 0 and email is not None:
            raise HTTPException(status_code=404, detail="Item not found")

        if top:
            return result[0]
        return result
