# Use Python 3.12.3 base image
FROM python:3.12.3-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend app code
COPY app/ ./app

# Set environment variables (optional if .env is mounted via Compose)
ENV PYTHONUNBUFFERED=1

# Expose Flask port
EXPOSE 5000

# Default command (you can change based on your __init__.py setup)
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
