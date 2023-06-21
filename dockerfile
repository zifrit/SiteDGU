FROM python:3.10

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY MainPartSiteDGU .
ENV DJANGO_SETTINGS_MODULE=MainPartSiteDGU.settings


EXPOSE 8000

CMD python manage.py migrate && \
    python manage.py collectstatic --noinput
