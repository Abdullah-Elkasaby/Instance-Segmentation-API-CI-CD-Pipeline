FROM python:3.9.16-slim-bullseye as builder

WORKDIR /app

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


# final stage
FROM python:3.9.16-slim-bullseye

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
COPY . /app
RUN pip install --no-cache /wheels/*

# FROM python:3.9.16-slim-bullseye as builder 

# WORKDIR /app

# COPY . /app

# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


# FROM builder
EXPOSE 8000
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80", "--workers", "2"]
