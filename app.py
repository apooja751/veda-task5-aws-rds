import os
import mysql.connector

db = mysql.connector.connect(
    host=os.environ["DB_HOST"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    database=os.environ["DB_NAME"]
)

cursor = db.cursor()

cursor.execute(
    "INSERT INTO test_table (message) VALUES (%s)",
    ("Hello from Python App - Veda Task 5",)
)

db.commit()

cursor.execute("SELECT * FROM test_table")

for row in cursor.fetchall():
    print(row)

cursor.close()
db.close()
