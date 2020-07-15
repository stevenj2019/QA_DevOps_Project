FROM python:3.8.4

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "usr/local/bin/python3", "server.py"]
