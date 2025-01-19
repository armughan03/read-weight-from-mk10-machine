# Set the base image to Python 3.11.11-alpine
FROM python:3.11.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the server code
COPY ./server .

# Run ruff to check the code
RUN ruff check
