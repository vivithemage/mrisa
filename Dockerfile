FROM python:3.7.5-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

CMD [ "python", "./server.py" ]

EXPOSE 5000
