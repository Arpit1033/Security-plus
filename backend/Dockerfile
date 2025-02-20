# Use an official Python image as base
FROM python:3.9

# Install libgl1 for OpenCV
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code
COPY . .

# Expose Flask's port
EXPOSE 5000

# Run Flask application
CMD ["python", "app.py"]
