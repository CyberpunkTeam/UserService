from app.models.users import User


def test_create_user():
    user = User(name="Martin", lastname="Diaz", email="mdiaz@gmail.com")
    assert user.name == "Martin"
    assert user.lastname == "Diaz"
    assert user.email == "mdiaz@gmail.com"
