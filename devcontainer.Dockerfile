FROM mcr.microsoft.com/devcontainers/python:3.12
RUN pip3 install --upgrade pip
RUN pip3 install poetry
WORKDIR /code 
COPY pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . /code