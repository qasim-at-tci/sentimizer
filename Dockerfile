FROM python:3.11.4-slim-bullseye

RUN apt update

WORKDIR /app

COPY . /app/

ENV FLASK_ENV=production
RUN pip install -r requirements.txt

EXPOSE 1111
CMD [ "gunicorn", "--config", "gunicorn_config.py", "app:app" ]
