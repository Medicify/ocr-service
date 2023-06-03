FROM python:3-slim

WORKDIR /product-service

COPY requirements.txt requirements.txt

RUN apt update && \
    pip3 install --upgrade pip && \
    pip3 install --no-cache-dir --upgrade -r /product-service/requirements.txt

COPY . ./

ENV PORT=5000
ENV DRUG_SERVICE_URL=http://34.36.211.221
ENV DEBUG=True

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5050"]