# write your dockerfile here

# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Give execute permission to run.sh
RUN chmod +x run.sh

# Make port 5001 available to the world outside this container
EXPOSE 5001

# use bash to run the run.sh script
CMD ["bash", "run.sh"]