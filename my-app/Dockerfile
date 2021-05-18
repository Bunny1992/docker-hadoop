# start from base
FROM ubuntu:18.04

LABEL maintainer="Nishant Bannikoppa <nishant.bannikoppa@esds.co.in>"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./templates/ /app/templates/
WORKDIR /app

COPY . /app
CMD [ "python", "./app.py" ]
