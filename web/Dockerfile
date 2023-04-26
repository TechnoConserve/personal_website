FROM python:3.10

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY wagtail-photography/ /wagtail-photography/
RUN ls -lah
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

RUN mkdir /app

RUN mkdir -p /app/media
RUN mkdir -p /app/static

RUN adduser -u 5678 --disabled-password --gecos "" appuser
RUN chown -R appuser:101 /app
RUN chmod -R 764 /app/media
RUN chmod -R 764 /app/static

WORKDIR /app
#USER appuser