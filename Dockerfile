FROM python:3.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --virtual .build-deps python-dev postgresql-dev musl-dev gcc
RUN apk add --no-cache libpq git

WORKDIR /BLST

COPY ./Pipfile /BLST/Pipfile
COPY ./Pipfile.lock /BLST/Pipfile.lock
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy


COPY . /BLST/

RUN apk del .build-deps