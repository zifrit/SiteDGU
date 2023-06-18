FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /test/dj

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY MainPartSiteDGU .

#EXPOSE 8000
#
#CMD ["python", "manage.py", "migrate"]
#CMD ["python", "manage.py", "runserver" , "0.0.0.0:8000"]