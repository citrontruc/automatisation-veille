
# ---------------
# Base générique
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS base

# Update the system packages
RUN apt -qy update && \
    apt -qy upgrade --no-install-recommends --no-install-suggests && \
    apt -qy clean && \
    rm -rf /var/lib/apt/lists

# Changement de fuseau horaire
RUN ln -fs /usr/share/zoneinfo/Europe/Paris /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# vidage du démarrage automatique
ENTRYPOINT []

# pour éviter les c/c malheureux
ARG PROJECT_ROOT=/api

# Applicatif
ENV PATH=${PROJECT_ROOT}/venv/bin:${PATH} \
    VIRTUAL_ENV=/opt/uv.venv \
    PYTHONPYCACHEPREFIX=/opt/python.cache \
    PYTHONPATH=${PROJECT_ROOT} \
    UV_CACHE_DIR=/opt/uv.cache \
    UV_PROJECT_ENVIRONMENT=/opt/uv.venv \
    UV_NO_CACHE=1 \
    UV_PYTHON=3.12.8 \
    UV_PYTHON_PREFERENCE=only-managed \
    UV_NO_ENV_FILE=0 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_NO_PROGRESS=1 \
    PROJECT_ROOT_ENV=${PROJECT_ROOT}

WORKDIR ${PROJECT_ROOT}
COPY --chown=root:root . .

RUN uv -q venv --seed &&\
    uv -q sync --frozen

# Create entry point to make the image executable
RUN chmod +x run.sh

CMD ["bash", "run.sh"]
