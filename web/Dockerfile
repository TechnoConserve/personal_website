FROM python:3.10

# We'll use this to figure out if we're testing or in production
ARG DJANGO_SETTINGS_MODULE

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY wagtail-photography/ /wagtail-photography/
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

RUN mkdir -p /app/media && \
    mkdir /app/static

COPY . /app

WORKDIR /app

# Install the wagtail-photography app from release if in production and remove the local wagtail-photography files
# Otherwise, install the local version
RUN if [ $DJANGO_SETTINGS_MODULE = "photo_blog.settings.production" ]; then \
      python -m pip install wagtail-photography && \
      rm -r /app/wagtail-photography; \
    else \
      python -m pip install ./wagtail-photography; \
    fi
