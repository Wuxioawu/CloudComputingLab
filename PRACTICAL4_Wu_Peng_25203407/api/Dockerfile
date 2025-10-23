# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy all API source code into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for the API
EXPOSE 8080

# Run FastAPI using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
