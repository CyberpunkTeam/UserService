from unittest.mock import Mock

import pytest
from fastapi import HTTPException

from app.controllers.user_controller import UserController
from app.models.users import Users


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
    result = UserController.get(repository, top=True)
    assert result.name == "Martin"


def test_get_user():
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
    result = UserController.get(repository, uid="1234", top=True)
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
    result = UserController.post(repository, user)
    assert result == user


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
        UserController.post(repository, user)
