# Use a base image with Python pre-installed
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose a port (if your project requires it)
# EXPOSE <port>

# Set the command to run your application
CMD [ "python", "app.py" ]
