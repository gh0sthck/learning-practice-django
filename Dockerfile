FROM python:3.12-alpine

ENV PYTHONBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' 

WORKDIR /practice/

COPY . /practice/

RUN pip install poetry
RUN poetry install --no-root --no-interaction --no-ansi

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
