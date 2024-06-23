# Use an official Python runtime as a parent image
FROM python:3.9.6

# Set the working directory in the container
WORKDIR /app

# Update package lists and install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev 

# Install any needed packages specified in requirements.txt
COPY req.txt .
RUN pip install -r req.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV SQLALCHEMY_DATABASE_URL=mysql+pymysql://root:@host.docker.internal/mekar

# Expose port 80 to allow communication to/from server
EXPOSE 80

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
