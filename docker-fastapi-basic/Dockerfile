# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn pydantic

# Expose port
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]