FROM python:3.10-slim

WORKDIR /app

# Install system libraries
RUN apt-get update && apt-get install -y gcc

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything (including model folder)
COPY . .

# Expose port
EXPOSE 8000

# Run API
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
