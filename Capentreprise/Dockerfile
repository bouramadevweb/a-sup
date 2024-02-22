# Select os
FROM python:3.12.1

# Generate python output
ENV PYTHONBUFFERED 1

# Create the root directory
RUN mkdir /app-root


# Set the working directory
WORKDIR /app-root

# Copy and link with my docker containerdocker
ADD . /app-root

# COPY static/ /app/static/
COPY requirements.txt /app-root/


# Execute requirements.txt
RUN pip install -r requirements.txt
