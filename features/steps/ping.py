from behave import *


@given("la app esta encendida")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("si le pego al /")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = context.client.get("/")


@then('recibo un mensaje de exito')
def step_impl(context):
    """
    :param message_content: String
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 200
