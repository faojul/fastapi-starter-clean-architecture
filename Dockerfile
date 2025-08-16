# Stage 1: Build stage
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential gcc libffi-dev

# Copy requirements and install in virtual environment
COPY requirements.txt .
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Stage 2: Runtime stage
FROM python:3.11-slim

WORKDIR /app

# Copy virtual environment and app code from builder
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /app /app

# Set PATH to use virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Command to run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
