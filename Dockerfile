FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=core/server.py

WORKDIR /app

COPY . .   

RUN pip install --no-cache-dir -r requirements.txt

RUN rm -f core/store.sqlite3
RUN flask db upgrade -d core/migrations/

EXPOSE 7755

CMD ["bash", "run.sh"]
