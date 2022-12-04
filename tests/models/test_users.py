from app.models.users import Users


def test_create_user():
    user = Users(
        name="Martin",
        lastname="Diaz",
        email="mdiaz@gmail.com",
        location="Buenos Aires",
        uid="1234",
    )
    assert user.name == "Martin"
    assert user.lastname == "Diaz"
    assert user.email == "mdiaz@gmail.com"
    assert user.uid == "1234"
