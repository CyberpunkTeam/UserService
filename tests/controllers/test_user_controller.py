from unittest.mock import Mock

import pytest
from fastapi import HTTPException

from app.controllers.user_controller import UserController
from app.models.agendas import Agendas
from app.models.users import Users
from app.models.response.users import Users as UsersResponse


def test_get_all_user():
    repository = Mock()
    repository.get.return_value = [
        Users(
            name="Martin",
            lastname="Lopez",
            email="tincho_lopez@gmail.com",
            location="CABA",
            uid="1234",
        ),
        Users(
            name="Juan",
            lastname="Gomez",
            email="juan_gomez@gmail.com",
            location="CABA",
            uid="1235",
        ),
    ]
    result = UserController.get(repository)
    assert len(result) == 2


def test_get_top_user():
    agenda_repository = Mock()
    agenda_repository.get.return_value = []
    repository = Mock()
    repository.get.return_value = [
        Users(
            name="Martin",
            lastname="Lopez",
            email="tincho_lopez@gmail.com",
            location="CABA",
            uid="1234",
        ),
        Users(
            name="Juan",
            lastname="Gomez",
            email="juan_gomez@gmail.com",
            location="CABA",
            uid="1235",
        ),
    ]
    result = UserController.get(
        repository, top=True, agenda_repository=agenda_repository
    )
    assert result.name == "Martin"


def test_get_user():
    agenda_repository = Mock()
    agenda_repository.get.return_value = []
    repository = Mock()
    repository.get.return_value = [
        Users(
            name="Martin",
            lastname="Lopez",
            email="tincho_lopez@gmail.com",
            location="CABA",
            uid="1234",
        )
    ]
    result = UserController.get(
        repository, uid="1234", top=True, agenda_repository=agenda_repository
    )
    assert result.name == "Martin"


def test_error_user_not_found():
    repository = Mock()
    repository.get.return_value = []
    with pytest.raises(HTTPException):
        UserController.get(repository, uid="4444", top=True)


def test_create_user():
    repository = Mock()
    repository.insert.return_value = True
    user = Users(
        name="Martin",
        lastname="Lopez",
        email="tincho_lopez@gmail.com",
        location="CABA",
        uid="1235",
    )
    user_response = UsersResponse(
        name="Martin",
        lastname="Lopez",
        email="tincho_lopez@gmail.com",
        location="CABA",
        uid="1235",
        followers=["mock"],
        following={"users": ["mock_uid"], "teams": ["mock_uid"]},
    )
    repository.get.return_value = [user]

    repository_agenda = Mock()
    agenda = Agendas(aid="mock", following_uid="mock_uid", agenda_type="USER")
    repository_agenda.get.return_value = [agenda]

    result = UserController.post(repository, user, repository_agenda)
    assert result.uid == user_response.uid


def test_error_create_user():
    repository = Mock()
    repository.insert.return_value = False
    user = Users(
        name="Martin",
        lastname="Lopez",
        email="tincho_lopez@gmail.com",
        location="CABA",
        uid="1234",
    )

    with pytest.raises(HTTPException):
        UserController.post(repository, user, repository)
