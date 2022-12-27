import random
import time
from datetime import datetime

import mongomock
from behave import *


@given("que no estoy registrado")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when(
    'completo el registro, con nombre "{name}", apellido "{lastname}", ubicaciones "{location}" y email "{email}"'
)
def step_impl(context, name, lastname, location, email):
    """
    ""
    :param name:
    :param lastname:
    :param location:
    :param email:
    :type context: behave.runner.Context
    """

    body = {
        "name": name,
        "lastname": lastname,
        "location": location,
        "email": email,
        "uid": "interal_uid",
    }
    context.vars["user_to_save"] = body


@step("confirmo el registro")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/users"

    context.response = context.client.post(
        url, json=context.vars["user_to_save"], headers=headers
    )


@then("se me informa que se registro exitosamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201
    user = context.response.json()
    local = datetime.now()
    assert user.get("created_date").split(":")[0] == local.strftime("%d-%m-%Y")
    assert user.get("updated_date").split(":")[0] == local.strftime("%d-%m-%Y")


@given(
    'que estoy registrado con nombre "{name}", apellido "{lastname}", ubicaciones "{location}" y email "{email}"'
)
def step_impl(context, name, lastname, location, email):
    """
    :param name:str
    :param lastname:str
    :param location:str
    :param email:str
    :type context: behave.runner.Context
    """
    body = {
        "name": name,
        "lastname": lastname,
        "location": location,
        "email": email,
        "uid": "1",
    }

    context.vars["user_before_update"] = body
    context.vars["uid_to_update"] = "1"
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/users"

    response = context.client.post(url, json=body, headers=headers)

    assert response.status_code == 201


@when(
    'actualizo mis datos a nombre "{name}", apellido "{lastname}", ubicaciones "{location}"'
)
def step_impl(context, name, lastname, location):
    """
    :param name:str
    :param lastname:str
    :param location:str
    :type context: behave.runner.Context
    """
    context.vars["user_to_update"] = {
        "name": name,
        "lastname": lastname,
        "location": location,
    }


@step("confirmo la actualizacion")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/users/" + context.vars["uid_to_update"]
    time.sleep(1)
    context.response = context.client.put(
        url, json=context.vars["user_to_update"], headers=headers
    )


@then("se me informa que se actualizo exitosamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 200


@step(
    'puedo ver que mi datos se actualizaron a nombre "{name}", apellido "{lastname}", ubicaciones "{location}"'
)
def step_impl(context, name, lastname, location):
    """
    :param name:str
    :param lastname:str
    :param location:str
    :type context: behave.runner.Context
    """

    url = "/users/" + context.vars["uid_to_update"]

    response = context.client.get(url)

    assert response.status_code == 200

    user_updated = response.json()
    context.vars["user_updated"] = user_updated
    user_before_update = context.vars["user_before_update"]

    assert user_updated.get("uid") == user_before_update.get("uid")
    assert user_updated.get("email") == user_before_update.get("email")
    assert user_updated.get("name") == name
    assert user_updated.get("lastname") == lastname
    assert user_updated.get("location") == location
    assert user_updated.get("created_date") < user_updated.get("updated_date")


@step(
    'cambio mi imagen de perfil a "{profile_image}" y mi imagen de portada a "{cover_image}"'
)
def step_impl(context, profile_image, cover_image):
    """
    :param profile_image: str
    :param cover_image: str
    :type context: behave.runner.Context
    """
    user_to_update = context.vars["user_to_update"]
    user_to_update["profile_image"] = profile_image
    user_to_update["cover_image"] = cover_image


@step('mi imagen es "{profile_image}" y mi imagen de portada es "{cover_image}"')
def step_impl(context, profile_image, cover_image):
    """
    :param profile_image: str
    :param cover_image: str
    :type context: behave.runner.Context
    """
    user_updated = context.vars["user_updated"]
    assert user_updated.get("cover_image") == cover_image
    assert user_updated.get("profile_image") == profile_image


@given(
    'que esta registrado el usuario con nombre "{name}", apellido "{lastname}", ubicaciones "{location}" y email "{email}"'
)
def step_impl(context, name, lastname, location, email):
    """
    :param name:str
    :param lastname:str
    :param location:str
    :param email:str
    :type context: behave.runner.Context
    """
    body = {
        "name": name,
        "lastname": lastname,
        "location": location,
        "email": email,
        "uid": f"{ random.randint(0, 1)}",
    }

    context.vars["user_before_update"] = body
    context.vars["uid_to_update"] = "1"
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/users"

    response = context.client.post(url, json=body, headers=headers)

    assert response.status_code == 201


@when('busco por "{search}"')
def step_impl(context, search):
    """
    :param search: str
    :type context: behave.runner.Context
    """
    url = f"/users/?search={search}"

    response = context.client.get(url)

    assert response.status_code == 200

    context.response = response


@then('me retorna como resultado el usuario con {field} "{value}"')
def step_impl(context, field, value):
    """
    :param field: str
    :param value: str
    :type context: behave.runner.Context
    """
    field2english = {"nombre": "name", "apellido": "lastname"}

    result = context.response.json()
    if len(result) == 1:
        user = result[0]
        assert user.get(field2english[field]) == value
    else:
        values = []
        for user in result:
            values.append(user.get(field2english[field]))

        assert value in values
