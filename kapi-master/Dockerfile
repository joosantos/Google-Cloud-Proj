# Use an official Python runtime as the base image
FROM python:3.10.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install necessary packages
#RUN apt-get update \
#    && apt-get install --no-install-recommends -y postgresql-client \
#    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the Python dependencies file
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry==1.8.2

# Install project dependencies using Poetry
RUN poetry install --no-root

# Copy the rest of the application code
COPY . .

# Expose the port on which the application will run
EXPOSE 8000

# Set environment variables
ENV DATABASE_URL postgres://postgres2:123@db-postgres-cloud-proj.a.aivencloud.com:11893/kapi?sslmode=require

# Command to run the backend server
CMD ["sh", "-c", "poetry install && poetry run uvicorn app:app --host 0.0.0.0 --port 8000"]
