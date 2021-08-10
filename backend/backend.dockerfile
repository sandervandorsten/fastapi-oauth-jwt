FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN python3 -m pip install python-multipart

WORKDIR /app/

COPY ./app /app

ENV PYTHONPATH=/app
