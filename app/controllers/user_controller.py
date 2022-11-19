from app.repositories.user_repository import UserRepository


class UserController:

    @staticmethod
    def get():
        return UserRepository.get()
