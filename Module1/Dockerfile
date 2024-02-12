# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}-slim as base

FROM base as development

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app
# Copy the source code into the container.
COPY . /app

RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:/app/.local/bin:$PATH"

# RUN poetry install --no-interaction --no-ansi
# RUN poetry update && poetry install
RUN poetry install

# Expose the port that the application listens on.
EXPOSE 5000

# Run the application.
# CMD poetry run gunicorn --bind 0.0.0.0 "app:create_app()"
ENTRYPOINT [ "poetry", "run", "--bind", "0.0.0.0:5000", "todo_app.app:create_app()" ]

FROM base as production

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app
# Copy the source code into the container.
COPY . /app

RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:/app/.local/bin:$PATH"

# RUN poetry install --no-interaction --no-ansi
RUN poetry update && poetry install

# Expose the port that the application listens on.
EXPOSE 5000

# Run the application.
# CMD poetry run gunicorn --bind 0.0.0.0 "app:create_app()"
ENTRYPOINT [ "poetry", "run", "gunicorn", "--bind", "0.0.0.0:5000", "todo_app.app:create_app()" ]