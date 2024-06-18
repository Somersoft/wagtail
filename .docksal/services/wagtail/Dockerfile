ARG PYTHON_IMAGE

FROM ${PYTHON_IMAGE}

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system packages required by Wagtail and Django.
# https://github.com/wagtail/wagtail/blob/v4.0.2/wagtail/project_template/Dockerfile
RUN apt-get update --yes --quiet \
&& apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    msmtp \
    curl \
 && rm -rf /var/lib/apt/lists/* \
 # From https://github.com/python-poetry/poetry
 && curl -sSL https://install.python-poetry.org/ | python

# Requirements are installed here to ensure they will be cached.
COPY ./pyproject.toml /pyproject.toml
COPY ./poetry.lock /poetry.lock
RUN /root/.local/bin/poetry install
ENV _PYTHON_VERSION=3.11
# ENV _PYTHON_VENV_PATH=`eval /root/.local/bin/poetry env info --path`
ENV _PYTHON_VENV_PATH=/root/.cache/pypoetry/virtualenvs/wagtail-app-il7asoJj-py$_PYTHON_VERSION
ENV PYTHONPATH=$_PYTHON_VENV_PATH/lib/python$_PYTHON_VERSION/site-packages

COPY ./services/wagtail/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./services/wagtail/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

EXPOSE 8000

WORKDIR /app

ENTRYPOINT ["/entrypoint"]

