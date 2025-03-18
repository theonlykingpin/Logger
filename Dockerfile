# Use a base image with Python pre-installed
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install NGINX and configure it
RUN apt-get update && apt-get install -y nginx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for NGINX
EXPOSE 80

# Set the command to start NGINX and Gunicorn
CMD ["sh", "-c", "service nginx start && gunicorn app:app -b 0.0.0.0:8000"]
