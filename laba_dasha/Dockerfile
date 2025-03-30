FROM python:3.9

RUN pip install flask

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py /app/app.py

WORKDIR /app

CMD ["python", "app.py"]
