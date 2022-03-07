FROM python:3.7
WORKDIR /code
COPY requirements.txt .
RUN pip install -r ./requirements.txt
COPY . .
CMD gunicorn simber_main.wsgi:application --bind 0.0.0.0:8000
