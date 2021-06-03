FROM python:3.8.2-slim-buster

copy . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py drf_create_token -r admin
RUN python manage.py drf_create_token -r test1
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]