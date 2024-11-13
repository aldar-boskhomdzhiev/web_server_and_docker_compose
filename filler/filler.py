import mysql.connector 
import time
import os 
import csv

def connect_to_db():
    while True:
        try:
            connection = mysql.connector.connect(
                host=os.getenv('DB_HOST'),
                port=int(os.getenv('DB_PORT')),
                user=os.getenv('MYSQL_USER'),
                password=os.getenv('MYSQL_PASSWORD'),
                database=os.getenv('MYSQL_DATABASE'),
                charset = 'utf8mb4',
                collation = 'utf8mb4_unicode_ci')
            return connection

        except mysql.connector.Error as e:
            time.sleep(5)


def fill_db(connection):
    with open('/app/data.csv','r',encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            name VARCHAR(255),
            age INT
        );
        """)

        for row in csv_reader:
            cursor.execute("INSERT INTO users (name, age) VALUES (%s,%s)",(row['name'],row['age']))
        connection.commit()
    

def display_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

if __name__== "__main__":
    conn = connect_to_db()
    fill_db(conn)
    display_data(conn)
    conn.close()
    