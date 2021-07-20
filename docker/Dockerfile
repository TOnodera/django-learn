FROM python:3.6.13-buster

RUN apt-get update && apt-get install -y git
RUN pip install flake8 autopep8
RUN pip install Django

WORKDIR /home/python/app
RUN useradd -u 1000 -om python && \
    chown -R python:python /home/python