ARG CLI_IMAGE

FROM ${CLI_IMAGE}

# Install additional apt packages
RUN set -xe; \
    apt-get update >/dev/null; \
    apt-get -y --no-install-recommends install >/dev/null \
    postgresql-client \
    pipx \
    python3.poetry \
    # Cleanup
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install base python libraries.
COPY ./base/pyproject.toml /pyproject.toml
COPY ./base/poetry.lock /poetry.lock
RUN /usr/bin/poetry install

ENV _PYTHON_VERSION=3.11
# ENV _PYTHON_VENV_PATH=`eval /root/.local/bin/poetry env info --path`
ENV _PYTHON_VENV_PATH=/home/docker/.cache/pypoetry/virtualenvs/wagtail-app-p9HyaoIY-py$_PYTHON_VERSION
ENV PYTHONPATH=$_PYTHON_VENV_PATH/lib/python$_PYTHON_VERSION/site-packages
