FROM python:latest

COPY . .
COPY ../requirements.txt . 

RUN pip3 install -r requirements.txt

EXPOSE 5002

ENTRYPOINT [ "usr/local/bin/python3" "api.py"]