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
    user_before_update = context.vars["user_before_update"]
    fields_updated = context.vars["user_to_update"]
    assert user_updated.get("uid") == user_before_update.get("uid")
    assert user_updated.get("email") == user_before_update.get("email")
    assert user_updated.get("name") == fields_updated.get("name")
    assert user_updated.get("lastname") == fields_updated.get("lastname")
    assert user_updated.get("location") == fields_updated.get("location")
