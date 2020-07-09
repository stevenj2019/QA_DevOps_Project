FROM python:latest

COPY . .
COPY ../requirements.txt . 

RUN pip3 install -r requirements.txt

EXPOSE 5001

ENTRYPOINT [ "usr/local/bin/python3" "api.py"]