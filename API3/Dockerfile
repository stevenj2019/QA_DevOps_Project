FROM python:latest

COPY . . 

RUN pip3 install flask

EXPOSE 5003

ENTRYPOINT [ "usr/local/bin/python3", "api.py"]