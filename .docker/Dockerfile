FROM python:3.7-slim-stretch

RUN apt-get update
RUN apt-get install -y libpq-dev build-essential

RUN pip install Django

RUN mkdir -p /home/django
COPY run.sh /home/django/run.sh
WORKDIR /home/django


RUN django-admin startproject webapp

ENV REQUIREMENTS_FILE=requirements.txt
ENV PACKAGES=Django

WORKDIR /home/django/webapp

EXPOSE 8000

CMD ["bash","/home/django/run.sh"]