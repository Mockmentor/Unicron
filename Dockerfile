FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./

RUN apt update && \
    apt install mecab && \
    pip install -r requirements.txt

COPY . .

ENV UNICRON_HOST='0.0.0.0'
ENV UNICRON_PORT=9000

CMD python server.py 