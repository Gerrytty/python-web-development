# Use an official Python image
FROM python:3.10-alpine

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5100

# Command to run the app
ENTRYPOINT ["python", "app.py"]