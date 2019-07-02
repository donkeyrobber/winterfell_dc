FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1


RUN apk update && \
    apk add postgresql-dev build-base gcc


COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    cd /tmp && \
    pip install -r requirements.txt

COPY . /app

WORKDIR /app

ENTRYPOINT ["python"]

CMD ["manage.py", "runserver", "0.0.0.0:8000"]