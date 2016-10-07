FROM python:3.5.1-alpine

ADD app.py /app.py

RUN pip install flask

EXPOSE 5000

ENTRYPOINT ["python", "/app.py"]
