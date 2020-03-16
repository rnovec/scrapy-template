# Dockerfile for Python App
#
# For more information about this section see:
# https://hub.docker.com/_/python

FROM python:3.6.6
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt