FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

ARG SERVICE_URL

ENV BOTANICAL_SERVICE_URL=$SERVICE_URL

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python"]

CMD [ "api.py" ]