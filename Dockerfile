FROM python:3-slim

WORKDIR /product-service

COPY requirements.txt requirements.txt

RUN apt update && \
    pip3 install --upgrade pip && \
    pip3 install --no-cache-dir --upgrade -r /product-service/requirements.txt

COPY . ./


ENV DB_HOST=172.31.112.3
ENV DB_USER=medicify
ENV DB_PASSWORD=Drugs123*
ENV DB_DATABASE=medicify_db

ENV PORT=5050

CMD ["uvicorn", "main:server", "--host", "0.0.0.0", "--port", "5050"]