FROM python:3.7.5-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apk add --update build-base curl-dev openssl-dev curl libxml2-dev libxslt-dev
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

CMD [ "python", "./server.py" ]

EXPOSE 5000