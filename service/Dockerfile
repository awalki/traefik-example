FROM ghcr.io/astral-sh/uv:python3.13-bookworm

COPY . /app

WORKDIR /app

RUN uv sync --frozen --no-cache

CMD ["uv", "run", "fastapi", "run", "--port", "8081", "--host", "0.0.0.0"]