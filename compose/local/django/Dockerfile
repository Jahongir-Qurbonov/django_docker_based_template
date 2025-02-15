FROM python:3.13-slim AS python

WORKDIR /usr/src/app

# Create devcontainer user and add it to sudoers
RUN addgroup --system app && adduser --system --group app

# Install additional dependencies
RUN apt-get update --fix-missing && \
    apt-get install --no-install-recommends -y \
    libc-dev \
    build-essential \
    python3-dev \
    libpq-dev \
    gettext \
    shared-mime-info \
    curl \
    ca-certificates && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Astral UV
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"
ENV UV_PROJECT_ENVIRONMENT="/usr/local/"

# Requirements are installed here to ensure they will be cached.
COPY ./pyproject.toml uv.lock ./

RUN uv pip install --upgrade pip setuptools wheel --system
RUN uv sync --dev

COPY ./compose/general/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start-django
RUN sed -i 's/\r$//g' /start-django
RUN chmod +x /start-django

COPY ./compose/general/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/general/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/general/django/celery/flower/start /start-celeryflower
RUN sed -i 's/\r$//g' /start-celeryflower
RUN chmod +x /start-celeryflower

# copy application code to WORKDIR
COPY . .

RUN chown -R app:app /usr/src/app

USER app

ENTRYPOINT ["/entrypoint"]
