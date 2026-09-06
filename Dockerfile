# Dockerfile

# syntax=docker/dockerfile:1

# =========================================================
# ➤ BASE STAGE
# =========================================================

# =========================
# 💿 Base image
# =========================

# Use official Python image
FROM python:3.14-slim AS base

# =========================
# 🔡 Environment
# =========================

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# =========================
# 📁 Working directory (WORKSPACE)
# =========================

# Set working directory
WORKDIR /workspace

# =========================
# 📦 SYSTEM DEPENDENCIES
# =========================

RUN apt-get update && apt-get install -y --no-install-recommends \
    make \
    && rm -rf /var/lib/apt/lists/*

# NOTE:
# Don't use like these below when install
#   make \
#   git \
#   # docker.io \
#   # docker-cli \
#   docker-ce-cli \
# Comments inside a \ continuation can produce unexpected parsing behavior.

# =========================
# 📄 Copy application
# =========================

COPY . .

# =========================
# 🚀 PYTHON SETUP
# =========================

RUN pip install --no-cache-dir --upgrade pip

# Optional PEP 440 version supplied by CI or a reviewed local build. Git metadata
# remains outside the Docker context, so setuptools-scm otherwise uses its
# configured fallback version.
ARG PHS_BUILD_VERSION


# =========================================================
# ➤ DEVELOPMENT STAGE
# =========================================================

# =========================
# 💿 DEVELOPMENT IMAGE
# =========================

FROM base AS development

# =========================
# 📦 Install DEV dependencies
# =========================

RUN if [ -n "$PHS_BUILD_VERSION" ]; then \
        SETUPTOOLS_SCM_PRETEND_VERSION="$PHS_BUILD_VERSION" \
            pip install --no-cache-dir -e ".[dev]"; \
    else \
        pip install --no-cache-dir -e ".[dev]"; \
    fi

# =========================
# 🚀 Default command
# =========================

ENTRYPOINT ["path-header-scanner"]

CMD ["--help"]


# =========================================================
# ➤ PRODUCTION STAGE
# =========================================================

# =========================
# 💿 PRODUCTION IMAGE
# =========================

FROM base AS production

# =========================
# 📦 INSTALL RUNTIME DEPENDENCIES
# =========================

RUN if [ -n "$PHS_BUILD_VERSION" ]; then \
        SETUPTOOLS_SCM_PRETEND_VERSION="$PHS_BUILD_VERSION" \
            pip install --no-cache-dir .; \
    else \
        pip install --no-cache-dir .; \
    fi

# Fail the build when runtime imports or CLI startup dependencies are missing.
RUN python -c "from app.cli.main import app"

# =========================
# 🚀 Default command
# =========================

ENTRYPOINT ["path-header-scanner"]

CMD ["--help"]
