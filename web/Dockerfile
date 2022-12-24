FROM python:3.8

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

RUN mkdir -p /app/media
RUN mkdir -p /app/static

RUN adduser -u 5678 --disabled-password --gecos "" appuser
RUN chown -R appuser:appuser /app
USER appuser