from app.models.users import Users


def test_create_user():
    user = Users(name="Martin", lastname="Diaz", email="mdiaz@gmail.com")
    assert user.name == "Martin"
    assert user.lastname == "Diaz"
    assert user.email == "mdiaz@gmail.com"
