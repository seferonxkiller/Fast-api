FROM ubuntu:latest
LABEL authors="programmer"

FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code

RUN pip install -r requirement.txt
COPY . /code/


ENTRYPOINT ["top", "-b"]