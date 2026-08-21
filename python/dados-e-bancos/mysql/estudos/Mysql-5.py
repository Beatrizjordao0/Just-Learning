import os
'''
the codex - Youtube Class
18/04/2024
Python and MySQL - Updating Entries and Limiting Queries
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
# This line of command will update to 7 where the data name is Bob
sqlCommand = 'UPDATE students SET age = 7 WHERE NAME = "Bob"'

# this command will be limiting my data to only 5
sqlCommand = 'SELECT * FROM students LIMIT 5'

# this will limit the fetch to 5 and will start 3 rows after the first one
sqlCommand = 'SELECT * FROM students LIMIT 5 OFFSET 3'

mycursor.execute(sqlCommand)

for student in mycursor:
    print(student)