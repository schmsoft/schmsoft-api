FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /schmsoft

WORKDIR /schmsoft

ADD . /schmsoft/

RUN pip install -r requirements.txt

