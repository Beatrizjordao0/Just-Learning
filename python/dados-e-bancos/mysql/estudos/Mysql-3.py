import os
'''
the codex - Youtube Class
18/04/2024
Python and MySQL - Selecting and Getting Data
'''

import mysql.connector

# initialize the database
mydb = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD", ""),
    database='testdb'
)

mycursor = mydb.cursor()
# execute command to get the data
mycursor.execute('SELECT name FROM students')
# store the data
myresult = mycursor.fetchall()     # fetch means 'buscar' so fetch all means 'buscar tudo'
# show the data         # we also can fetchone, which will return for us only the first column of our table
for row in myresult:
    print(row)