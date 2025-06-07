FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /code

# dépendances Python minimalistes
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# code du projet
COPY . .

CMD ["gunicorn", "immo.wsgi:application", "--bind", "0.0.0.0:8000"]
