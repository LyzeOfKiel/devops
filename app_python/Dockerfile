FROM python:3.9.6-alpine3.14

WORKDIR /app

RUN adduser --disabled-password app && chown -R app /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER app

EXPOSE 8000

CMD ["-c", "gunicorn.conf.py"]

ENTRYPOINT ["gunicorn"]
