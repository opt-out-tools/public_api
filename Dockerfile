FROM python:3.7.4-slim-buster

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=0.12.17

RUN apt-get update && apt-get install -y \
     build-essential \
     curl \
     gcc \
     gettext \
     git \
     libffi-dev \
     musl-dev \
     libpq-dev \
     postgresql-contrib \
     tini \
     libhdf5-serial-dev \
     gfortran \
     liblapack-dev \
     && pip install -U "pip<19.0" \
     && pip install "poetry==$POETRY_VERSION"

RUN poetry config settings.virtualenvs.create false

WORKDIR /usr/src/app
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
RUN touch README.md

RUN mkdir -p /usr/src/app/src/opt_out && touch /usr/src/app/src/opt_out/__init__.py
RUN poetry install --no-interaction --no-ansi --no-dev
RUN pip install gunicorn

COPY README.md README.md
COPY src src
COPY manage.py manage.py


ENTRYPOINT ["tini", "--"]

CMD python manage.py migrate  &&  gunicorn opt_out.public_api.website.wsgi:application --workers 2 --bind 0.0.0.0:8000