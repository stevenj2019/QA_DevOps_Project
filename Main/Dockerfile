FROM python:latest

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

ARG PROD_DB_URI
ARG PROD_SKEY
ENV PROD_DB_URI $PROD_DB_URI
ENV PROD_SKEY $PROD_SKEY
ENTRYPOINT [ "usr/local/bin/python3", "server.py"]