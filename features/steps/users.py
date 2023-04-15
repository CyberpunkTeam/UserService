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
        "uid": f"{ random.randint(0, 100)}",
    }

    context.vars["user_before_update"] = body
    context.vars["uid_to_update"] = "1"
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/users"

    response = context.client.post(url, json=body, headers=headers)
    user = response.json()
    context.vars[body.get("name") + "_uid"] = user.get("uid")
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


@when(
    'actualizo mis experiencia laboral a {action} en "{company}" como "{position}" desde "{start_date}"'
)
def step_impl(context, action, company, position, start_date):
    """
    :param action:str
    :param company:str
    :param position:str
    :param start_date:str
    :type context: behave.runner.Context
    """
    current_job = True if action == "trabajo" else False

    work_experience = context.vars.get("work_experience", [])
    work_experience.append(
        {
            "current_job": current_job,
            "company": company,
            "position": position,
            "start_date": start_date,
        }
    )
    context.vars["user_to_update"] = {"work_experience": work_experience}
    context.vars["work_experience"] = work_experience


@step("puedo ver que mis dos experiencias cargadas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    user = context.response.json()
    assert len(user.get("work_experience")) == 2


@step("puedo ver que mi educacion")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    user = context.response.json()
    assert len(user.get("education")) == 2


@when(
    'actualizo mi educacion a que {action} en el colegio "{institution}" {title} en sociales desde "{start_date}" '
    'hasta "{finish_date}"'
)
def step_impl(context, action, institution, title, start_date, finish_date):
    """
    :param action:str
    :param institution:str
    :param title:str
    :param start_date:str
    :param finish_date:str
    :type context: behave.runner.Context
    """
    finished = True if action == "estudio" else False

    education = context.vars.get("education", [])
    education.append(
        {
            "institution": institution,
            "title": title,
            "start_date": start_date,
            "finish_date": finish_date,
            "finished": finished,
        }
    )
    context.vars["user_to_update"] = {"education": education}
    context.vars["education"] = education


@step(
    'actualizo mi educacion a que {action} en la "{institution}" {title} desde "{start_date}"'
)
def step_impl(context, action, institution, title, start_date):
    """
    :param action:str
    :param institution:str
    :param title:str
    :param start_date:str
    :param finish_date:str
    :type context: behave.runner.Context
    """
    finished = True if action == "estudio" else False

    education = context.vars.get("education", [])
    education.append(
        {
            "institution": institution,
            "title": title,
            "start_date": start_date,
            "finished": finished,
        }
    )
    context.vars["user_to_update"] = {"education": education}
    context.vars["education"] = education


@when('"{follower_name}" sigue a "{following_name}"')
def step_impl(context, follower_name, following_name):
    """
    :type context: behave.runner.Context
    """
    follower_uid = context.vars[follower_name + "_uid"]
    following_uid = context.vars[following_name + "_uid"]
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = f"/users/{following_uid}/followers/{follower_uid}"

    response = context.client.post(url, headers=headers)
    assert response.status_code == 201


@then('"{follower_name}" aparace entre los seguidos de "{following_name}"')
def step_impl(context, follower_name, following_name):
    """
    :type context: behave.runner.Context
    """
    follower_uid = context.vars[follower_name + "_uid"]
    following_uid = context.vars[following_name + "_uid"]
    url = f"/users/{following_uid}"

    response = context.client.get(url)
    assert response.status_code == 200

    user = response.json()
    followers = user.get("followers")
    assert follower_uid in followers


@step('"{follower_name}" tiene entre sus seguidos a "{following_name}"')
def step_impl(context, follower_name, following_name):
    """
    :type context: behave.runner.Context
    """
    follower_uid = context.vars[follower_name + "_uid"]
    following_uid = context.vars[following_name + "_uid"]
    url = f"/users/{follower_uid}"

    response = context.client.get(url)
    assert response.status_code == 200

    user = response.json()
    following = user.get("following")
    assert following_uid in following
