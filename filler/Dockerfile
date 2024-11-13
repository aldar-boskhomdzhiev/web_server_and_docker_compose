FROM python:3.9-slim

RUN pip install mysql-connector-python
COPY filler.py /app/filler.py

WORKDIR /app

CMD ["python3","filler.py"]
