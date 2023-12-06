# Instructions:
# sudo docker build -t daimo-image .
# sudo docker run -d -p 8080:8080 daimo-image

# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Clone the Git repository
RUN apt-get update && \
    apt-get install -y git && \
    git clone https://github.com/jsurrea/DAIMO.git

# Change the working directory to /app/DAIMO
WORKDIR /app/DAIMO

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port that your FastAPI app will run on
EXPOSE 8080

# Command to run the application
CMD ["python3", "app.py"]