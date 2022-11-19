pip install poetry

poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

coverage run --source=app -m behave
coverage run -a --source=app -m pytest tests/

coveralls