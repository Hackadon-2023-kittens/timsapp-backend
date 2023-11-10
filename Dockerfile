# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /timsapp-backend

RUN pip3 install flask flask-cors

COPY . .

CMD [ "python3", "main.py"]