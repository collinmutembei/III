FROM python:3.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /BLST

RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /BLST/Pipfile
RUN pipenv install --deploy --system --skip-lock --dev


COPY . /BLST/
