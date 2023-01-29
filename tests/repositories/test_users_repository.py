import mongomock

from app import config
from app.models.education import Education
from app.models.users import Users
from app.models.work_experience import WorkExperience
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


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_get_users_list():
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

    user = Users(
        name="Matias",
        lastname="Fonseca",
        location="CABA",
        email="mfonseca@fi.uba.ar",
        uid="2234",
    )

    ok = repository.insert(user)

    assert ok

    user = Users(
        name="Matias",
        lastname="Fonseca",
        location="CABA",
        email="mfonseca@fi.uba.ar",
        uid="4444",
    )

    ok = repository.insert(user)

    assert ok

    uids_list = ["2234", "1234"]

    users_returned = repository.get_by_list(uids_list)

    assert len(users_returned) == 2

    assert users_returned[0].uid == uids_list[0]
    assert users_returned[1].uid == uids_list[1]



@mongomock.patch(servers=(("server.example.com", 27017),))
def test_get_user_with_education_and_work_experience():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = UsersRepository(url, db_name)

    education_high_school = Education(
        title="Bachiller",
        institution="San jose",
        start_date="2001-02-01",
        finish_date="2019-02-01",
        finished=True,
    )
    education_collage = Education(
        title="Informatic engineering",
        institution="UBA",
        start_date="2019-02-01",
        finished=False,
    )

    work_expirience_1 = WorkExperience(
        position="Jr data scientist",
        company="Mercado Libre",
        start_date="2019-02-01",
        finish_date="2020-02-01",
        current_job=False,
    )

    work_expirience_2 = WorkExperience(
        position="SR data scientist",
        company="Mercado Libre",
        start_date="2020-02-01",
        current_job=True,
    )

    user = Users(
        name="Matias",
        lastname="Fonseca",
        location="CABA",
        email="mfonseca@fi.uba.ar",
        uid="1234",
        education=[education_high_school, education_collage],
        work_experience=[work_expirience_1, work_expirience_2],
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
    assert len(user_found.education) == 2
    assert len(user_found.work_experience) == 2
