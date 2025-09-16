FROM python:3.13-slim

WORKDIR /app

RUN apt-get update \
  && apt-get install -y gcc libpg-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

RUN mkdir -p /app/media

EXPOSE 8000