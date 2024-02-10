# syntax=docker/dockerfile:1
FROM python:3.11.5-slim-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY . .

RUN bash -c "pip install --upgrade pip"
RUN bash -c "pip install -r requirements.txt"

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]