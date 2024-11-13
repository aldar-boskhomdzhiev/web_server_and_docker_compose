from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import mysql.connector 
import time

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

def get_db_connection():
    
    while True:
        try:
            connect= mysql.connector.connect(
                    host=os.getenv('DB_HOST'),
                    port=int(os.getenv('DB_PORT')),
                    user=os.getenv('MYSQL_USER'),
                    password=os.getenv('MYSQL_PASSWORD'),
                    database=os.getenv('MYSQL_DATABASE'),
                    charset = 'utf8mb4',
                    collation = 'utf8mb4_unicode_ci')
            return connect
        except mysql.connector.Error as e:
            time.sleep(5)


@app.get("/",response_model=list[User])
def get_all_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    connection.close()
    return users


@app.get("/health")
def health_check():
    return {"status":"OK"}


@app.get("/{item_id}")
def not_found(item_id:Union[int, str] = None):
    raise HTTPException(status_code=404)

