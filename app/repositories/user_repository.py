from app.models.user import User


class UserRepository:

    @staticmethod
    def get():
        return [User(name="Martin",
                     lastname="Lopez",
                     email="tincho_lopez@gmail.com"),
                User(name="Juan",
                     lastname="Gomez",
                     email="juan_gomez@gmail.com")]
