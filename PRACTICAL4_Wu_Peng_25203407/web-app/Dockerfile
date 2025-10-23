# Use Python 3.9 slim as base image
FROM python:3.9-slim

# Create a working directory inside the container
WORKDIR /app

# Copy all source files from current directory to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 inside the container
EXPOSE 5000

# Run the web app when the container starts
CMD ["python", "app.py"]

