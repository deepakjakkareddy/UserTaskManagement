FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY . .

# Install system dependencies and Python libraries
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    pip install --no-cache-dir psycopg2 Flask==2.3.2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Expose the application port
EXPOSE 5001

# Command to run the application
CMD ["python", "task_service.py"]
