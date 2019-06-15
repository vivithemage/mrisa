FROM ubuntu:18.04

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

## Remain current
RUN apt-get update -qq \
	&& apt-get dist-upgrade -y

RUN apt-get install git python3 virtualenv -y
RUN git clone https://github.com/vivithemage/mrisa.git && \
    cd mrisa && \
    python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV && \
    pip install -r requirements.txt;

RUN cd mrisa && python src/server.py

EXPOSE 5000
