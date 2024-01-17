FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install ffmpeg -y && \
    pip install sentence_transformers && \
    pip install openai-whisper &&\
    pip install grpcio &&\
    pip install protobuf &&\
    pip install pandas

COPY . .

ENV UNICRON_HOST='0.0.0.0'
ENV UNICRON_PORT=9000

CMD python server.py 
