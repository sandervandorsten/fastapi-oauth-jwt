FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN python3 -m pip install --upgrade pip && python3 -m pip install setuptools

WORKDIR /app/

COPY ./app/requirements.txt app/requirements.txt

RUN python3 -m pip install -r app/requirements.txt

COPY ./app /app

ENV PYTHONPATH=/app
