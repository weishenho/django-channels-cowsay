FROM python:2-onbuild
ENV PYTHONUNBUFFERED 1
ENV REDIS_HOST "redis"
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN apt-get update
RUN apt-get -y install fortune cowsay
ENV PATH="/usr/games:${PATH}"
RUN pip install -r requirements.txt
RUN python manage.py migrate
