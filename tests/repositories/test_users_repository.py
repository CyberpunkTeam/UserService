import mongomock

from app import config
from app.models.users import Users
from app.repositories.users_repository import UsersRepository


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_save_user():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = UsersRepository(url, db_name)

    user = Users(
        name="Matias",
        lastname="Fonseca",
        location="CABA",
        email="mfonseca@fi.uba.ar",
        uid="1234",
    )

    ok = repository.insert(user)

    assert ok


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_get_user():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = UsersRepository(url, db_name)

    user = Users(
        name="Matias",
        lastname="Fonseca",
        location="CABA",
        email="mfonseca@fi.uba.ar",
        uid="1234",
    )

    ok = repository.insert(user)

    assert ok

    users_found = repository.get("1234")

    assert len(users_found) == 1

    user_found = users_found[0]

    assert user_found.name == "Matias"
    assert user_found.lastname == "Fonseca"
    assert user_found.location == "CABA"
    assert user_found.email == "mfonseca@fi.uba.ar"
    assert user_found.uid == "1234"
