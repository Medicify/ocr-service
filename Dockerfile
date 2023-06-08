FROM python:3-slim

WORKDIR /ocr-service

COPY requirements.txt requirements.txt

RUN apt update && \
    pip3 install --upgrade pip && \
    pip3 install --no-cache-dir --upgrade -r /ocr-service/requirements.txt

COPY . ./


ENV DB_HOST=localhost
ENV DB_USER=
ENV DB_PASSWORD=
ENV DB_DATABASE=

ENV PORT=5050

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5050"]