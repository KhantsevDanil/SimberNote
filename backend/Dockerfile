FROM python:3.7-slim
WORKDIR /code
COPY requirements.txt .
RUN pip install -r ./requirements.txt
COPY . .
CMD ["gunicorn", "simbir_main.wsgi:application", "--bind", "0:8000" ]
