pip install poetry

poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

pre-commit install
pre-commit run
