FROM python:latest

COPY . .
COPY ../requirements.txt . 

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "usr/local/bin/python3" "server.py"]