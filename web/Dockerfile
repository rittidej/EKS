FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /code     
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]