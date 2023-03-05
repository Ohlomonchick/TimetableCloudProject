FROM python:3.11-slim-buster

COPY ./timetable_django ./app
COPY ./requirements.txt ./app

WORKDIR /app

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install wheel --upgrade && \
    /opt/venv/bin/pip install pip -r requirements.txt && \
    chmod +x entrypoint.sh

EXPOSE 8000

CMD [ "/app/entrypoint.sh" ]