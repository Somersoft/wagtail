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
