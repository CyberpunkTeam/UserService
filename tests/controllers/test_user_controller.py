from unittest.mock import patch

from app.controllers.user_controller import UserController
from app.models.user import User


@patch('app.repositories.user_repository.UserRepository.get', return_value=[User(name="Martin",
                                                                                 lastname="Lopez",
                                                                                 email="tincho_lopez@gmail.com"),
                                                                            User(name="Juan",
                                                                                 lastname="Gomez",
                                                                                 email="juan_gomez@gmail.com")])
def test_get_all_user(mock_repository):
    result = UserController.get()
    assert len(result) == 2
