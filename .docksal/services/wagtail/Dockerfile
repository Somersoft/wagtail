ARG PYTHON_IMAGE

FROM ${PYTHON_IMAGE}

# Install additional apt packages for bookworm distribution
RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		postgresql-client \
		python3-poetry \
	; \
	rm -rf /var/lib/apt/lists/*

# Install base python libraries.
COPY ./base/pyproject.toml /pyproject.toml
COPY ./base/poetry.lock /poetry.lock
RUN /usr/bin/poetry install

ENV _PYTHON_VERSION=3.11
# ENV _PYTHON_VENV_PATH=`poetry env info --path`;
# ENV PYTHONPATH=$_PYTHON_VENV_PATH/lib/python$_PYTHON_VERSION/site-packages
ENV PYTHONPATH=/root/.cache/pypoetry/virtualenvs/wagtail-app-il7asoJj-py$_PYTHON_VERSION/lib/python$_PYTHON_VERSION/site-packages

COPY --chmod=777 ./services/wagtail/entrypoint ./services/wagtail/start /
RUN sed -i 's/\r$//g' /entrypoint
RUN sed -i 's/\r$//g' /start

EXPOSE 8000

WORKDIR /var/www/${DOCROOT}

ENTRYPOINT ["/entrypoint"]
