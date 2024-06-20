# Use an official Python runtime as a parent image
FROM python:2.7

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED 1

# Run manage.py collectstatic to gather static files
RUN python ./library_system/manage.py collectstatic --noinput


