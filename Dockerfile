# Base Python image
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy everything to the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set env variables from .env
ENV PYTHONUNBUFFERED=1

# Default command: run scheduler
CMD ["python", "scheduler.py"]
