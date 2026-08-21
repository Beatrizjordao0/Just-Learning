import os
'''
the codex - Youtube Class
18/04/2024
Python and MySQL - Deleting Entries and Dropping Tables
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

# Deletes from the table students the name Rachel in name column
sqlCommand = 'DELETE FROM students WHERE name = "Rachel"'

# We can do the same with intengers like age
sqlCommand = 'DELETE FROM students WHERE age = 44'

# With this MySQL command we erase the whole table students
sqlCommand = 'DROP TABLE students'

# IF EXISTS command will only delete the table if it exists, if not, nothing will happen
sqlCommand = 'DROP TABLE IF EXISTS students'

mycursor.execute(sqlCommand)

mydb.commit()