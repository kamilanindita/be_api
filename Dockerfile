FROM python:3.8.3-alpine

#  lxml requires libxml2 and libxslt to be installed
RUN apk add --update --no-cache g++ gcc libxml2-dev libxslt-dev

# set work directory
WORKDIR /app

# set environment variables
# prevents Python from copying pyc files to the container.
ENV PYTHONDONTWRITEBYTECODE 1
#ensures that Python output is logged to the terminal, making it possible to monitor Django logs in realtime.
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /app

RUN pip install -r requirements.txt

# copy project
COPY . /app

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]