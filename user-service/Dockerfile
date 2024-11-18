FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY . .

# Install system dependencies for PostgreSQL and psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc && apt-get clean
RUN pip install --no-cache-dir psycopg2 Flask

# Expose the application port
EXPOSE 5002

CMD ["python", "user_service.py"]
