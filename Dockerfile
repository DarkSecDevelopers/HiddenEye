FROM debian:10
LABEL MAINTAINER="Equinockx moisestapia741@gmail.com"

WORKDIR /home/

COPY . /home/

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3.7 && \
    apt-get install -y python3-pip && \
    apt-get install --no-install-recommends -y php && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt
