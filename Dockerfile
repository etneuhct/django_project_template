FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PYSETUP_PATH="/opt/pysetup" \
    POETRY_HOME="/opt/poetry" \
    POETRY_VERSION=1.2.0

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update \
    && apt-get install --no-install-recommends -y curl libpq-dev build-essential nginx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3

WORKDIR /usr/src/app
COPY pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction  --no-root
RUN rm -rf /root/.cache/pypoetry
COPY . .
RUN python manage.py collectstatic

COPY docker/proxy_default.conf /etc/nginx/conf.d/django_app.conf
CMD sh ./.docker/runme.sh
