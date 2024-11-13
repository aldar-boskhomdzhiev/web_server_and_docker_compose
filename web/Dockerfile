FROM python:3.9-slim

RUN pip install mysql-connector-python uvicorn fastapi
COPY web.py /app/web.py

WORKDIR /app
EXPOSE 8000

CMD ["uvicorn", "web:app", "--host", "0.0.0.0", "--port", "8000"]
