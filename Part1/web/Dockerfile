FROM python
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:80", "--wsgi-file", "wsgi.py", "--callable", "app"]
