ARG CLI_IMAGE

FROM docksal/cli:php8.3

# Install additional apt packages
RUN set -xe; \
    apt-get update >/dev/null; \
    apt-get -y --no-install-recommends install >/dev/null \
    postgresql-client \
    # Cleanup
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
