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
