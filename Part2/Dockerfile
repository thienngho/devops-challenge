FROM python:2.7.13-alpine

WORKDIR /app
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

VOLUME /var/run/docker.sock
COPY check_tags.py /app

CMD ["python", "check_tags.py"]
