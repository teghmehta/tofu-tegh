FROM python:3.9-alpine

WORKDIR /code

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 4000

CMD ["python", "app.py"]
